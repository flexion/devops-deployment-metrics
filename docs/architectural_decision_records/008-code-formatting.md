# 8. Code Formatting

Date: 2019-07-07

## Status

Accepted

## Context

Proper code formatting is vital to the long-term viability and maintainability of a code base.
A codebase with consistent formatting reduces cognative burden on developers because it is:

- Easier to review
- Easier to diff against previous commits
- More likely to be free of linting errors

## Decision

- We use [Black](https://github.com/python/black) as code formatter for Python.
- We use Black's default options.
- We CI to ensure PRs are appropriately formatted before being accepted.
- We require and document the setup of `Black`, `prettier`, `flake8`, and `reorder-python-imports` in the development
  environment through pre-commit hooks.

## Consequences

These decisions are supported by our use of the [Hypermodern Python cookiecutter](https://github.com/cjolowicz/cookiecutter-hypermodern-python).

In a minor change from the Hypermodern Python cookiecutter, the import order is handled by `reorder-python-imports` rather
than `isort`.
