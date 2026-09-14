# 20. Use rumdl instead of markdownlint-cli for Markdown linting

Date: 2026-09-14

## Status

Accepted

## Context

We lint Markdown as part of the pre-commit hooks run in CI ([ADR 006](006-ci-linting.md)), using
`markdownlint-cli` (`ghcr.io/igorshubovych/markdownlint-cli:v0.31.1`) via pre-commit's `docker_image` language. This
means every pre-commit run -- locally and in CI -- has to pull and start a Docker container just to lint Markdown,
which is slow compared to the rest of the hooks (all native/Python), and adds a Docker dependency to the toolchain for
a purely local Node.js CLI tool.

[rumdl](https://github.com/rvben/rumdl) is a Rust reimplementation of markdownlint with a native pre-commit hook (no
Docker required -- pre-commit installs it via `pip` into an isolated environment) and claims drop-in rule
compatibility, including automatic discovery of existing `.markdownlint.json`/`.markdownlintignore` files and a
built-in `rumdl import` command to convert them to its own TOML format.

Options considered:

1. **Do nothing** -- keep `markdownlint-cli` and its Docker dependency.
2. **Adopt rumdl** -- a maintained, native reimplementation with equivalent rule coverage.

## Decision

Replace the `markdownlint-cli` Docker hook in `.pre-commit-config.yaml` with the
[`rumdl-pre-commit`](https://github.com/rvben/rumdl-pre-commit) hook (`id: rumdl`, no `docker_image` language).

`.markdownlint.json` and `.markdownlintignore` are replaced by `.rumdl.toml`:

- `"line-length": false` becomes `disable = ["MD013"]`.
- `"MD024": {"siblings_only": true}` is kept explicit under `[MD024]`, even though it now matches rumdl's default.
- The three files listed in `.markdownlintignore` (`docs/contributing.md`, `docs/index.md`, `docs/codeofconduct.md`)
  become `exclude` entries; rumdl's pre-commit hook respects `.rumdl.toml`'s `exclude` even for the changed files
  pre-commit passes explicitly.
- `docs/usage.md` and `docs/reference.md` embed Sphinx `` ```{eval-rst} `` code fences; rumdl's default ("standard")
  flavor doesn't recognize `{name}` as a fence language and flags MD040, so these two files are pinned to rumdl's
  `myst` flavor via `[per-file-flavor]`, which treats `{name}` as a valid directive info string.
- The existing `<!-- markdownlint-configure-file ... -->` inline directive in `docs/threat-model.md` needed no
  change -- rumdl supports `markdownlint-*` inline comments for compatibility.

Running the new hook against the existing docs also surfaced a handful of real, pre-existing issues, fixed alongside
this change: a broken relative link in [ADR 006](006-ci-linting.md), a non-descriptive `[here](...)` link in
`README.md`, and a broken `[MIT license]` reference link in `README.md` (its definition was labeled `[license]`,
which doesn't match).

## Consequences

### Positive

- No Docker pull/startup on the Markdown lint hook; pre-commit installs rumdl natively (Rust binary via `pip`),
  matching the speed of the rest of the hooks.
- One less Docker dependency in the local/CI toolchain.
- Rule coverage is a superset of the previous config (`MD053`, `MD057`, `MD059`, ... are enabled by default in rumdl
  and aren't part of classic `markdownlint-cli`), which caught real issues on adoption.

### Negative

- rumdl's default rule set isn't a byte-for-byte match of `markdownlint-cli`'s (e.g. rule defaults differ, and some
  rules like `MD053`/`MD057`/`MD059` don't exist in the old tool at all), so future adoption of a new markdownlint
  ruleset elsewhere won't automatically stay in sync with this repo's `.rumdl.toml`.
- rumdl is a newer, smaller project than `markdownlint-cli`; if it stops being maintained we'd need to revisit this
  decision.
