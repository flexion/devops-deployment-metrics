# 4. Use GitHub Actions for CI/CD

Date: 2023-04-07

## Status

Accepted.

## Context

GitHub Actions are a mature product. GitHub Actions integrate well with our version control system GitHub. In addition, there are
[mature tools](https://github.com/nektos/act) to test GitHub actions as well as an Action linter [actionlint-docker](https://github.com/rhysd/actionlint).

## Decision

We will use [GitHub Actions](https://github.com/features/actions) to run our CI/CD processes.

### Consequences

These decisions are supported by our use of the [Hypermodern Python cookiecutter](https://github.com/cjolowicz/cookiecutter-hypermodern-python).

GitHub Actions for OSS projects run on shared runners, so sometimes there is a wait for the CI to start.
