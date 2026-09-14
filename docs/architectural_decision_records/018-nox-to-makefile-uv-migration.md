# Replace Nox with a Makefile and Direct uv Invocations for Task Running

## Context

Since [ADR 016](https://github.com/flexion/devops-deployment-metrics/blob/main/docs/architectural_decision_records/016-use-uv-instead-of-poetry.md),
`pyproject.toml` has used PEP 621 project metadata, PEP 735 `[dependency-groups]`, and a committed `uv.lock` — all
uv-native. `noxfile.py`, inherited from the original hypermodern-python cookiecutter (ADR 010), still owned actual
task execution: each session (`tests`, `pre-commit`, `pip-audit`, `xdoctest`, `docs-build`, `benchmark`, ...) built
its own throwaway virtualenv and re-declared its own tool list, duplicating what `[dependency-groups]` already
specified. CI installed both `uv` and `nox` via `pipx` just to run `nox --python=X` with a `NOXSESSION` environment
variable selecting the session — a layer of indirection nox added value to (per-session isolated venvs, multi-Python
matrixing) that we weren't actually using, since Python-version matrixing was already done by the GitHub Actions
matrix, not by nox itself.

## Decision

We will remove `noxfile.py` and replace it with:

1. A **Makefile** at the repo root, whose targets (`test`, `coverage`, `lint`, `audit`, `xdoctest`, `docs`,
   `docs-serve`, `benchmark`, `typecheck`) wrap `uv run` / `uv sync`, for local developer convenience — this is the
   moral equivalent of nox's session list, without nox's per-session venv machinery, sourced from the same
   `[dependency-groups]` uv already manages.
2. **CI workflows that do not invoke `make`.** Each GitHub Actions job runs the same underlying `uv run <tool>`
   command directly (`.github/workflows/tests.yml`'s per-session `run:` step selects the right command with a shell
   `case` statement; `benchmark.yaml` runs its `uv run pytest --benchmark-json=...` line directly).

The second point was a correction made during implementation: our first pass had CI call `make <target>` for
consistency with local dev. That broke the `windows-latest` matrix row — GitHub's Windows runner image does not
ship GNU Make on `PATH` (confirmed against the `actions/runner-images` Windows Server 2022 software inventory),
whereas nox, being pure Python, worked identically across `ubuntu-latest` and `windows-latest` without any extra
install step. `uv` itself is fully cross-platform, so calling it directly avoids reintroducing an OS-specific gap,
without adding a new install step (e.g. `choco install make`) that would also require widening the
`step-security/harden-runner` egress allowlist (see ADR 015) for another package CDN — the kind of allowlist drift
that has already caused a CI outage once in this repo.

## Alternatives Considered

1. **Keep nox as a thin wrapper over uv** (sessions reduced to `uv sync` + `uv run <tool>` one-liners).
   - Pros: smallest diff; keeps `nox -s <session>` muscle memory; nox already handles Python-version selection.
   - Cons: still a tool + a pipx bootstrap step in CI providing no capability we use once its sessions are this thin.

2. **Makefile everywhere, including CI** (what we initially implemented).
   - Pros: one command surface (`make <target>`) for both humans and CI.
   - Cons: breaks on `windows-latest`, which has no GNU Make on `PATH`; fixing that by installing Make in CI adds a
     new dependency and a new CDN endpoint to allowlist, for a tool CI doesn't otherwise need.

3. **Makefile for humans; CI calls `uv run` directly** (chosen).
   - Pros: CI has no dependency on Make at all, so it's identical across every runner OS; no new allowlist entries;
     `make` stays available locally as a convenience layer documented in CONTRIBUTING.md.
   - Cons: the mapping from "session name" to "uv command" now exists in two places (the Makefile, and the `case`
     statement in `tests.yml`) instead of one; they must be kept in sync by hand when a session's command changes.

## Consequences

### Positive Impacts

- CI no longer installs or depends on nox, removing a tool and a `pipx install` step from every job.
- CI has no dependency on GNU Make either, so behavior is identical across `ubuntu-latest` and `windows-latest`
  without OS-specific install steps or a wider `harden-runner` allowlist.
- Local development gets a conventional, low-ceremony `make <target>` interface instead of nox's session model.
- Dev tooling versions come from one place (`[dependency-groups]` in `pyproject.toml` + `uv.lock`) instead of being
  re-declared per nox session.

### Negative Impacts

- The session→command mapping is duplicated between the Makefile and `tests.yml`'s `case` statement; a change to one
  (e.g. adding a new flag to the test command) must be mirrored in the other or they'll drift.
- Losing nox also loses its automatic multi-Python-version session fan-out; that responsibility now rests entirely
  on the GitHub Actions matrix (which was already doing the actual version selection).

## Status

Accepted

## Consequences of Not Making This Change

- CI would keep paying the cost of installing and invoking nox for sessions that no longer need nox's isolation or
  multi-version capabilities.
- Nox sessions would keep silently drifting from `[dependency-groups]`, since each session declares its own tool
  versions rather than reading the group uv already manages.
