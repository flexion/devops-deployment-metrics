# 15. Use Step Security for GitHub Actions Runner Hardening

## Date

2024-06-21

## Status

Approved

## Context

Our CI/CD pipelines utilize GitHub Actions to automate builds, tests, and deployments. Ensuring the security of these
pipelines is crucial to protect our codebase and sensitive data from potential security threats.

## Decision

Our CI/CD pipelines utilize GitHub Actions to automate builds, tests, and deployments. Ensuring the security of these
pipelines is crucial to protect our codebase and sensitive data from potential security threats.

## Options Considered

1. **Do Nothing**: Continue using GitHub Actions without additional security measures.
2. **Custom Security Implementation**: Develop our own security hardening scripts and policies.
3. **Use Step Security**: Implement Step Security’s GitHub Action runner hardening.

## Decision Drivers

- **Security**: We need to enhance the security of our GitHub Actions runners to protect against unauthorized access and
- vulnerabilities.
- **Simplicity**: We prefer a solution that is easy to implement and maintain without extensive custom development.
- **Compliance**: We need to meet specific security compliance requirements.
- **Cost**: We aim for a cost-effective solution.

## Decision Outcome

We have chosen to use Step Security’s GitHub Action runner hardening. This decision is based on the following reasons:

- **Enhanced Security**: Step Security provides a comprehensive set of security features that address our needs for
- environment isolation, least privilege, network restrictions, and more.
- **Ease of Use**: The solution integrates seamlessly with our existing GitHub Actions workflows with minimal
- configuration effort.
- **Compliance and Auditability**: Step Security provides detailed audit logs and helps ensure compliance with
- security standards.
- **Cost-Effective**: Using a third-party solution saves us time and resources compared to developing and maintaining
- custom security scripts.

## Consequences

### Positive

- Improved Security: Our CI/CD pipelines will have enhanced protection against security threats.
- Simplified Compliance: Easier to meet security compliance requirements.
- Reduced Development Effort: Leveraging a third-party solution saves time and resources.

### Negative

- Dependency on Third-Party: We will rely on Step Security for updates and maintenance of the security features.

## Review

This decision will be reviewed periodically to ensure it continues to meet our security and operational needs.
