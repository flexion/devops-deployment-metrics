# 8. Code Formatting

Date: 2024-03-07

## Status

Accepted

## Context

Proper code formatting is vital to the long-term viability and maintainability of a code base.
A codebase with consistent formatting reduces cognative burden on developers because it is:

- Easier to review
- Easier to diff against previous commits
- More likely to be free of linting errors

## Decision

- We use [ruff](https://docs.astral.sh/ruff/formatter/) as code formatter for Python.
- We use `ruff` provides `black`-compatible default options.
- We CI to ensure PRs are appropriately formatted before being accepted.
- We require and document the setup of `ruff` and `prettier` in development.
- `ruff` provides faster `flake8` and `isort` functionality in the development
  environment through pre-commit hooks.

## Consequences

These decisions are supported by our use of the [Hypermodern Python cookiecutter](https://github.com/cjolowicz/cookiecutter-hypermodern-python).
