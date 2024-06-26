# DevOps Deployments Metrics

[![PyPI](https://img.shields.io/pypi/v/devops-deployment-metrics.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/devops-deployment-metrics.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/devops-deployment-metrics)][python version]
[![License](https://img.shields.io/pypi/l/devops-deployment-metrics)][license]

[![Read the documentation at https://devops-deployment-metrics.readthedocs.io/](https://img.shields.io/readthedocs/devops-deployment-metrics/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/flexion/devops-deployment-metrics/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/flexion/devops-deployment-metrics/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/devops-deployment-metrics/
[status]: https://pypi.org/project/devops-deployment-metrics/
[python version]: https://pypi.org/project/devops-deployment-metrics
[read the docs]: https://devops-deployment-metrics.readthedocs.io/
[tests]: https://github.com/flexion/devops-deployment-metrics/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/flexion/devops-deployment-metrics
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

An application that generates DevOps deployment metrics from GitHub repositories using a GitHub Action workflow to deploy a product.

## Three deployment metrics

This application reads historical data for workflows from GitHub. The application looks at records for the deployment workflow
and generates Deployment Frequency, Change Fail Percentage and a Mean Time to Recover metrics for fixed-width reporting periods.

Metrics will be reported from a configured starting time to the present, with results reported in fixed-width periods.
The reporting period width is configurable from 1 day on up.

### Deployment Frequency

Deployment Frequency is a simple calculation of the number of successful deployments per day in the reporting period. For example,
if there is a 14-day reporting period, and there are 28 successful deployments by the workflow during that period, the deployment
frequency would be 2.0.

### Change Fail Rate

Change Fail Rate is a simple ratio of the number of failed deployments over the total number of deployments in a given
reporting period, expressed as a percentage. If all the deployments fail, the change fail rate will be 100.0. If all the
deployments succeed, the change fail rate will be 0.0.

### Mean Time to Recover

The deployment Mean Time to Recover (MTTR) mean of the deployment time-to-recover in a given reporting period.
The deployment time-to-recover is the time between a failed deployment and the next successful deployment. The
metric is reported in hours.

## Features

- Generates CSV files with deployment frequency, deployment change-fail percentage and deployment mean time to recover metrics.
- Generates CSV file with deployment log record

## Requirements

- Python 3.9+
- Poetry (installation instructions provided [here](https://python-poetry.org/docs/#installing-with-the-official-installer))
- Supported OS: Windows 10, Windows 11, Linux, MacOS

## Installation

```shell
poetry install
```

## Usage

### Create a configuration file

A configuration file must be created and passed to the application at run time.

#### Sample file: my-config.toml

```text

    # Keys
    title = "Sample devops-deployment-metrics configuration"

    [general]
        time-slice-days = 7
        start-date = 2023-09-01T00:00:01
        date-format = "%Y-%m-%d"
        timezone = "UTC"

    [[repositories]]
        owner = "ccsq-isfcs"
        repo = "security-findings-lambda"
        workflow_filename = "cicd.yaml"
        deployment-frequency = "df"
        change-fail-rate = "cfr"
        mean-time-to-recover = "mttr"
        deployment-log = "deployments"

```

#### Field Description

**time-slice-days:** duration used to group metric data
**start-date:** the start date of metric collection (end date is automatically assumed to be current day)
**owner:** Github organization name
**repo:** repository name
**workflow_filename:** GitHub Action workflow filename for the workflow that deploys the product.
Just the filename, not the path.

### Launching the application

```shell
poetry run devops-deployment-metrics -v -c my-config.toml
```

Please see the [Command-line Reference] for more details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license],
_DevOps Deployments Metrics_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/flexion/devops-deployment-metrics/issues

<!-- github-only -->

[license]: https://github.com/flexion/devops-deployment-metrics/blob/main/LICENSE
[contributor guide]: https://github.com/flexion/devops-deployment-metrics/blob/main/CONTRIBUTING.md
[command-line reference]: https://devops-deployment-metrics.readthedocs.io/en/latest/usage.html
