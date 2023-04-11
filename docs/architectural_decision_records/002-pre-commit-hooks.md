# 2. Use pre-commit hooks before commiting to version control

Date: 2023-04-07

## Status

Accepted

## Context

Git hook scripts are useful for identifying simple issues before submission to code review. Linters, code quality and
security scanners should be applied to the codebase and run successfully before committing code to a pull request.

## Decision

Use pre-commit to standardize linters and scanners

Create a `.pre-commit-config.yaml` that provides a consistent set of pre-commithooks. Versions should generally be explicit within
that file to avoid ambiguity. Clear instructions should be provided to enable
new developers and reviewers to quickly and efficiently utilize the solution.
Instructions should be provided so that basic `pre-commit` expectations for
developers are clear.

## Consequences

These decisions are supported by our use of the [Hypermodern Python cookiecutter](https://github.com/cjolowicz/cookiecutter-hypermodern-python).

When pre-commit linters are used, code will be consistently formatted and mistakes will be caught sooner, leading to higher quality code.
