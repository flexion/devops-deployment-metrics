# 19. Use zizmor for static security analysis of GitHub Actions workflows

Date: 2026-09-14

## Status

Accepted

## Context

We already lint GitHub Actions workflows with `actionlint` via pre-commit ([ADR 006](006-ci-linting.md)), and we harden
every runner with Step Security's `harden-runner` ([ADR 015](015-github-action-runner-hardening.md)). Neither of these
catches security-specific anti-patterns in workflow YAML itself: script injection via untrusted `${{ }}` expressions
interpolated into `run:` blocks, overly broad `permissions:`, unpinned third-party actions, or paths that can exfiltrate
secrets. `actionlint` is syntax/style-focused; `harden-runner` protects the runner's network egress at execution time
but doesn't statically flag risky workflow authoring patterns before they run.

`flexion/flexion-opp-capture` already runs `zizmor`, a purpose-built static analyzer for GitHub Actions workflows and
composite actions, in its CI (dedicated `harden-runner` + `astral-sh/setup-uv` + `uvx zizmor` job). zizmor is
actively maintained, distributed as an installable CLI (no new language/package-manager surface -- it runs via `uv`,
which we've already standardized on, [ADR 016](016-use-uv-instead-of-poetry.md)), and ships auto-fixes for several of
its findings.

Options considered:

1. **Do nothing** -- keep relying on `actionlint` and `harden-runner` alone.
2. **Build custom checks** -- write our own scripts/regexes for these anti-patterns.
3. **Adopt zizmor** -- a maintained, purpose-built static analyzer for exactly this problem.

## Decision

Add a dedicated `zizmor` CI job ([`zizmor.yml`](../../.github/workflows/zizmor.yml)) that runs
`uvx zizmor==<pinned version> --min-severity high .github/workflows` on pull requests, pushes to `main`, and
`workflow_dispatch`. The job is pinned (exact zizmor version, `astral-sh/setup-uv` action SHA) and runs behind
`harden-runner`, matching every other job in this repo. `--min-severity high` fails the build on real issues while
staying quiet about lower-confidence/stylistic findings (zizmor's default "regular" persona already minimizes false
positives).

Adopting this job immediately surfaced one real high-severity finding -- a spoofable `github.actor` bot-identity
check in the dependabot auto-merge workflow -- which was fixed as part of the same change
(see [devops-deployment-metrics-8gd](https://github.com/flexion/devops-deployment-metrics/issues)).

## Consequences

### Positive

- Security-focused coverage of workflow YAML that `actionlint`'s syntax/style linting doesn't provide.
- Caught and fixed a real spoofable-actor-check vulnerability on adoption.
- Minimal new footprint: one CI job, no new package manager, reuses `uv`/`uvx` we already depend on.

### Negative

- One more CI job and one more pinned version (`zizmor==<version>`) to keep current; unlike our Python
  dependencies, this pin isn't tracked by Dependabot, so it needs periodic manual bumps.
- `--min-severity high` means medium/low findings (e.g. the `artipacked` "missing `persist-credentials: false`"
  warnings currently present across several workflows) won't fail CI and need separate follow-up tracking so they
  don't go stale.
