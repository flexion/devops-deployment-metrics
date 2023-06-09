# Threat model

Initial threat model for `devops-deployments-metrics`.

## Unauthorized Access

### Threat

Unauthorized users gaining access to the CLI application or sensitive information provided during runtime.

### Mitigation

Implement strong authentication and access controls to ensure only authorized users can execute the CLI application and
access sensitive data. Consider utilizing secure token-based authentication or API keys.

The application utilizes secure communication with GitHub over TLS.

## Command Injection

### Threat

Attackers injecting malicious commands through user input, leading to unintended execution of arbitrary code.

### Mitigation

Apply proper input validation and sanitization techniques to prevent command injection attacks. Use parameterized queries
or prepared statements when executing commands or interacting with external systems.

CodeQL does provide some static code analysis of code in this project.

To do: review inputs for injection risk and mitigate findings.

## Insecure Credential Handling

### Threat

Improper handling of user credentials, such as GitHub username and password, leading to potential exposure or compromise.

### Mitigation

Implement secure credential management practices, such as securely storing credentials, avoiding hard-coding them within
the source code, and utilizing secure credential storage mechanisms like environment variables or secret management
solutions. Ensure that sensitive credentials, such as the GitHub username and password, are properly protected and encrypted.

We are running [gitleaks](https://github.com/flexion/devops-deployment-metrics/blob/main/docs/architectural_decision_records/005-secrets-detection.md)
in `pre-commit` hooks and in the CI/CD workflow to reduce the risk of storing credentials in the repository.

Contributors to the project and users of this library should follow secure coding best practices and use a secure password manager.

## Logging of Sensitive Information

### Threat

Sensitive information, such as GitHub tokens or configuration details, being logged or exposed in logs, leading to potential
unauthorized access.

### Mitigation

Ensure that sensitive information is not logged or masked in log outputs. Implement proper log filtering and review
logging configurations to avoid exposing sensitive data.

Contributors to the project and users of this library should follow secure coding best practices for logging.

## Lack of Input Validation for Configuration

### Threat

Improper or malicious configuration files leading to unexpected behavior or security vulnerabilities.

### Mitigation

Implement robust input validation and strict parsing of the configuration file to prevent arbitrary code execution or
unintended behavior. Validate and sanitize user-provided configuration inputs to mitigate potential security risks.

CodeQL does provide some static code analysis of code in this project.

To do: review configuration inputs for injection risk and mitigate findings.

## Insufficient input validation for the `connect_to_github` function

### Mitigation

Implement robust input validation and strict parsing of inputs for the `connect_to_github` function. Validate and sanitize
user-provided inputs to mitigate potential security risks, such as ensuring the `username` and `password` inputs adhere
to the expected format and length to avoid potentially malicious inputs.

To do: review `connect_to_github` inputs for injection risk and mitigate findings.

## Insecure Communication

### Threat

Insecure transmission of sensitive data, such as GitHub credentials, over the network.

### Mitigation

Use secure communication protocols, such as HTTPS, when communicating with external services or APIs. Encrypt sensitive
data during transmission to prevent eavesdropping or interception.

The application utilizes secure communication with GitHub over TLS.

## Lack of Error Handling

### Threat

Insufficient error handling and reporting, leading to potential information disclosure or denial of service.

### Mitigation

Implement comprehensive error handling mechanisms to catch and handle exceptions properly. Avoid displaying detailed
error messages to end users, as they may reveal sensitive information.

To do: extend error handling as new axes of change emerge.

## Inadequate Testing Coverage

### Threat

Insufficient testing coverage may lead to undetected vulnerabilities or unreliable behavior.

### Mitigation

Implement a robust testing strategy that includes unit tests, integration tests, and security testing. Perform comprehensive
testing to identify and fix bugs, vulnerabilities, and potential issues.

To do: add integration tests

Contributor are expected to improve the code as they contribute, adding tests for all changed code, as well
as following secure coding practices.

The `Nox` build process includes some [security scanning with `Safety`](https://github.com/flexion/devops-deployment-metrics/blob/main/docs/architectural_decision_records/009-dependency-scanning.md).
The definition of done for user stories includes security assessment and a code coverage standard.

## Insider Threats

### Threat

Authorized users with malicious intent exploiting their privileges to misuse or compromise the CLI application or sensitive data.

### Mitigation

Implement proper access controls, least-privilege principles, and regular auditing to detect and prevent insider threats.
Regularly review and monitor user activities and permissions to identify any suspicious behavior.

The contributions to the project are monitored by the repository owner.

Users of the library are responsible within their own sphere of influence.

## Insecure Communication

### Threat

Insecure transmission of sensitive data, such as GitHub credentials, over the network.

### Mitigation

Use secure communication protocols, such as HTTPS, when communicating with external services or APIs. Encrypt sensitive
data during transmission to prevent eavesdropping or interception.

The application utilizes secure communication with GitHub over TLS.

## Insecure Data Storage (Metric Output Files)

### Threat

Insecure storage of metric output files, potentially exposing sensitive information or allowing unauthorized access.

### Mitigation

Ensure that the metric output files are securely stored, utilizing appropriate file permissions and encryption. Implement
access controls and authentication mechanisms to restrict access to the metric output files to authorized users or processes.

Users of the library should follow best practices for securing the metric output files.

## Insecure Logging Configuration

### Threat

Insecure logging configuration that may expose sensitive information or provide attackers with insights into the
application's internal workings.

### Mitigation

Implement secure logging practices, such as carefully configuring log levels and avoiding logging sensitive information.
Ensure that logging output is properly protected and inaccessible to unauthorized users. Regularly review and monitor log
files to detect any suspicious activities or signs of unauthorized access.

Contributors to the project and users of this library should follow secure coding best practices for logging.
Users of the library should use safe configuration files.

## Insecure Log Storage

### Threat

Insecure storage of log files, potentially exposing sensitive information or allowing unauthorized access.

### Mitigation

Ensure that log files are securely stored, utilizing appropriate file permissions and encryption. Implement access controls
and authentication mechanisms to restrict access to log files to authorized users or processes. Regularly monitor and
rotate log files to prevent them from becoming a target for attackers or consuming excessive storage space.

Users of the library should use secure storage for log files.

## Lack of Input Validation for Logging Configuration

### Threat

Insufficient input validation for the logging configuration, allowing for potentially malicious inputs that may alter
the logging behavior or cause log injection attacks.

### Mitigation

Implement robust input validation and strict parsing of the logging configuration. Validate and sanitize user-provided
inputs to mitigate potential security risks, such as ensuring that the logging configuration file is properly formatted
and contains only trusted configuration settings.

To do: review input validation for the logging configuration inputs for injection risk and mitigate findings.

## Insecure Access to Log Files

### Threat

Unauthorized access or disclosure of log files, leading to potential exposure of sensitive information or valuable
insights into the application's behavior.

### Mitigation

Implement strong access controls for log files, including file permissions and proper user/group management. Ensure that
log files are only accessible to authorized users or processes and are protected from unauthorized reading, modification,
or deletion. Regularly monitor and review access logs for log file access patterns to detect any suspicious activities.

Users of the library should follow best practices for securing the logging files.

## Unauthorized Access to GitHub Workflows

### Threat

Unauthorized access to GitHub workflows, allowing attackers to manipulate or interfere with the deployment process or
gain insights into the application's deployment metrics.

### Mitigation

Implement proper access controls and authentication mechanisms for GitHub workflows. Ensure that only authorized individuals
or systems have the necessary permissions to modify or execute workflows. Regularly review and monitor access logs
for any unauthorized access attempts or suspicious activities related to the workflows.

To do: assess workflow access risk from non-authorized users and mitigate.

## Manipulation of Workflow Data

### Threat

Manipulation or tampering of workflow data, leading to inaccurate deployment metrics or unauthorized changes to the
deployment process.

### Mitigation

Implement data integrity checks and validation mechanisms for workflow data. Use secure channels and encryption to protect
the communication between the application and GitHub workflows. Implement proper authentication and authorization checks
to ensure that the workflow data is not modified or tampered with by unauthorized entities.

The application utilizes secure communication with GitHub over TLS.

## Insecure Storage of Workflow Credentials

### Threat

Insecure storage of credentials or sensitive information used by the workflows, potentially leading to unauthorized
access to repositories or other resources.

### Mitigation

Implement secure storage mechanisms for workflow credentials, such as using encrypted secrets or secure key management
systems. Avoid hard-coding sensitive information directly in the workflows and utilize secure environment variables or
secret management solutions. Regularly review and audit the usage of credentials to ensure their proper protection and
minimize the risk of exposure.

Workflow files are linted by [actionlint](https://github.com/flexion/devops-deployment-metrics/blob/main/docs/architectural_decision_records/006-ci-linting.md).

To do: assess workflow access risk workflows and mitigate.

## Lack of Input Validation for Workflow Parameters

### Threat

Insufficient input validation for workflow parameters, allowing for potentially malicious inputs that may alter the
behavior of workflows or introduce security vulnerabilities.

### Mitigation

Implement strict input validation and sanitization for workflow parameters. Validate and sanitize user-provided inputs
to mitigate potential security risks, such as ensuring that branch names, URLs, or other input values are properly
formatted and do not contain malicious payloads or characters that could lead to command injection or other attacks.

Workflow files are linted by [actionlint](https://github.com/flexion/devops-deployment-metrics/blob/main/docs/architectural_decision_records/006-ci-linting.md).

To do: assess workflow access risk workflows and mitigate.

<!-- markdownlint-configure-file { "MD024": false } -->
