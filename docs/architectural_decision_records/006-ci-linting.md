# 6. Linting in the CI pipeline

Date: 2023-04-07

## Status

Accepted

## Context

Consistently and well-formatted code is [easier to read, diff and maintain](docs/architectural_decision_records/008-code-formatting.md).
Running linting in the continuous integration (CI) process makes sure developers are following the rules.

## Decision

Run the pre-commit hooks that run the code formatters and linters duing the CI process.

## Consequences

These decisions are supported by our use of the [Hypermodern Python cookiecutter](https://github.com/cjolowicz/cookiecutter-hypermodern-python).
