# 5. Use GitLeaks for secrets detection

Date: 2023-04-07

## Status

Accepted

## Context

We want to dynamically scan the repository for secrets before code is checked in and after code is checked in.
There are a number of secrets detection tools that run from the command line and are suitable for running locally
in the development environment as well as in a GitHub Action CI process.

Recently the IBM `detect-secrets` ecosystem has been unstable.
A similar tool `gitleaks` has the advantage of being able to look at Git history in a way it seems `detect-secrets` cannot.

## Decision

Use `gitleaks` for secrets detection in this project.

## Consequences
