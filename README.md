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

- TODO

## Installation

```shell
poetry install
```

## Usage

```shell
poetry run devops-deployment-metrics -v -c my-config.toml
```

Please see the [Command-line Reference] for more details.

### How to find the workflow id

To find the workflow id value for the configuration file, you can add the correct value for owner and repo and any string
for the id

```toml
[[repositories]]
    owner = "my-owner"
    repo = "my-repo"
    id = "dog-cow"
```

Then run in debug mode:

```shell
 poetry run devops-deployment-metrics -d -c my-config.toml
```

It will fail with an error.
Now you can search the log for the value of the `id` you will need. Search the log for the JSON object for your production
deployment workflow. Within that object find the value for `workflow_id` and add that to your configuration file.

```toml
[[repositories]]
    owner = "my-owner"
    repo = "my-repo"
    id = "12345678"
```

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
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/flexion/devops-deployment-metrics/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/flexion/devops-deployment-metrics/blob/main/LICENSE
[contributor guide]: https://github.com/flexion/devops-deployment-metrics/blob/main/CONTRIBUTING.md
[command-line reference]: https://devops-deployment-metrics.readthedocs.io/en/latest/usage.html
