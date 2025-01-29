# Replace Safety with pip-audit for Dependency Vulnerability Scanning

## Context

When using open-source third-party libraries as dependencies in our application, it is crucial to make sure these
dependencies do not contain security vulnerabilities. The standard tools for this do software composition analysis
(SCA).

Our project has relied on **Safety** to perform vulnerability scans on Python dependencies, per
[ADR 009](https://github.com/flexion/devops-deployment-metrics/blob/main/docs/architectural_decision_records/009-dependency-scanning.md).
Safety has historically been a widely used tool for identifying security issues in dependencies by checking them against
a vulnerability database. However, recent changes to the Safety tool have introduced new complexities:

- **Commercialization**: Safety's developer has moved toward a more commercial model, making some features that were
  previously free more restrictive.
- **Increased Complexity**: The usage and integration of Safety in CI/CD pipelines have become more cumbersome due to
  changes in its licensing and API access.
- **Limited Value**: For our purposes, we need a simple, fast, and reliable vulnerability scanner that integrates
  seamlessly into our existing workflows without introducing new barriers.

Given these changes, it no longer makes sense to continue using Safety. We need a replacement that provides similar
functionality with minimal disruption.

## Decision

We will replace **Safety** with **pip-audit** for dependency vulnerability scanning.

## Rationale for Choosing pip-audit

**pip-audit** is a tool developed by the Python Packaging Authority (PyPA) to perform dependency vulnerability checks
by analyzing installed packages and comparing them against the Python Package Index (PyPI) vulnerability database. It
serves as a direct drop-in replacement for Safety with several key advantages:

- **Open Source and Community-Driven**: pip-audit is maintained by the PyPA, ensuring that it remains an open and
  community-driven tool.
- **No Additional Licensing Requirements**: Unlike Safety, pip-audit does not require any commercial licensing or
  special API access.
- **Simplicity**: The tool is straightforward to use and integrates well with existing workflows. It does not introduce
  unnecessary complexity.
- **Accurate Vulnerability Data**: pip-audit leverages the PyPI advisory database to provide accurate and up-to-date
  vulnerability information.
- **Drop-in Replacement**: The command-line usage of pip-audit is similar to Safety, making the transition easy without
  significant changes to our CI/CD configuration.

## Consequences

### Positive Impacts

- **Simplified Workflow**: pip-audit requires fewer steps to configure and does not have any commercial limitations.
- **Cost Savings**: By using an open-source solution, we avoid potential licensing fees associated with Safety.
- **Improved Integration**: pip-audit integrates smoothly with our existing tooling, including GitHub Actions and other
  CI/CD platforms.
- **Community Support**: As a PyPA project, pip-audit has a strong backing from the Python community, ensuring long-term
  viability.

### Negative Impacts

- **New Tool Familiarization**: Team members will need to become familiar with pip-audit’s command-line interface and
  output format.
- **Potential Gaps in Data**: The vulnerability database used by pip-audit may differ slightly from the one used by
  Safety, though both tools are generally reliable.

## Status

Supersedes [ADR 009](https://github.com/flexion/devops-deployment-metrics/blob/main/docs/architectural_decision_records/009-dependency-scanning.md)

## Consequences of Not Making This Change

If we continue using Safety:

- We will face increasing complexity in managing vulnerability scans.
- We risk paying for features that were previously free.
- Our workflows will become harder to maintain, potentially impacting productivity.

By making this change, we ensure that our project remains secure, cost-effective, and simple to manage.
