# 9. Scan dependencies with software composition analysis tools

Date: 2023-04-07

## Status

Deprecated by [ADR 017](https://github.com/flexion/devops-deployment-metrics/blob/main/docs/architectural_decision_records/017-pip-replaces-safety.md)

## Context

When using open-source third-party libraries as dependencies in our application, it is crucial to make sure these
dependencies do not contain security vulnerabilities. The standard tools for this do software composition analysis (SCA).

Snyk offers SCA scanning, with CLI and as SaaS options. GitHub offers SCA for files in the repostory.
Semgrep Supply Chain detects recently discovered security vulnerabilities in your codebase for OSS.
Safety is an OSS SCA tool designed for Python projects.

Running dependency checks on each pull request and as a scheduled scan is a best practice, as emerging vulnerabilities
may be discovered the repository is not active.

## Decision

Run Safety scans in CI and as a nightly build, to scan the Python applications.

## Consequences

These decisions are supported by our use of the [Hypermodern Python cookiecutter](https://github.com/cjolowicz/cookiecutter-hypermodern-python).

Builds will break when vulnerabilities are found.
