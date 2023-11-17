# Contributor Guide

Thank you for your interest in improving this project.
This project is open-source under the [MIT license] and
welcomes contributions in the form of bug reports, feature requests, and pull requests.

Here is a list of important resources for contributors:

- [Source Code]
- [Documentation]
- [Issue Tracker]
- [Code of Conduct]

[mit license]: https://opensource.org/licenses/MIT
[source code]: https://github.com/flexion/devops-deployment-metrics
[documentation]: https://devops-deployment-metrics.readthedocs.io/
[issue tracker]: https://github.com/flexion/devops-deployment-metrics/issues

## How to report a bug

Report bugs on the [Issue Tracker].

When filing an issue, make sure to answer these questions:

- Which operating system and Python version are you using?
- Which version of this project are you using?
- What did you do?
- What did you expect to see?
- What did you see instead?

The best way to get your bug fixed is to provide a test case,
and/or steps to reproduce the issue.

Please label your bug report with the `bug` label.

## How to request a feature

Request features on the [Issue Tracker].

## How to set up your development environment

If you're interested in contributing code, you can start by checking out this repository
[https://github.com/flexion/devops-deployment-metrics](https://github.com/flexion/devops-deployment-metrics).
Take a look through the issues and see if there are any tasks you are interested in working on.
Indicate you are working on a task by adding your GitHub @name after the task in the issue.
Definition of Done items are often a great starting point for contributing in a meaningful way while getting integrated into team practices.
Using SSH keys to check out the repository is ideal, as we require contributors to sign their commits.

You need Python 3.9+ and the following tools:

- [Poetry]
- [Nox]
- [nox-poetry]

Install the package with development requirements:

```console
poetry install
```

You can now run an interactive Python session,
or the command-line interface:

```console
poetry run python
poetry run devops-deployment-metrics
```

[poetry]: https://python-poetry.org/
[nox]: https://nox.thea.codes/
[nox-poetry]: https://nox-poetry.readthedocs.io/

### Git pre-commit hooks

In order to ensure a consistent style for a number of different artifact types within this repository, all developers
should install, initialize, and run `pre-commit` in their development environment. Committing code and documentation
that does not pass the pre-commit checks is strongly discouraged. Instructions for doing so are below, with more details
at [https://pre-commit.com/#install](https://pre-commit.com/#install):

You can install pre-commit with pip:
`pip install pre-commit`

Or on a Mac you can use homebrew:
`brew install pre-commit`

After installation, set up the git hook scripts by running the following from the root of the repository:
`pre-commit install`

The pre-commit hooks will then run as a part of git commits, but you can also optionally run them against all files:
`pre-commit run --all-files`

## How to test the project

Run the full test suite:

```console
nox
```

List the available Nox sessions:

```console
nox --list-sessions
```

You can also run a specific Nox session.
For example, invoke the unit test suite like this:

```console
nox --session=tests
```

Unit tests are located in the _tests_ directory,
and are written using the [pytest] testing framework.

[pytest]: https://pytest.readthedocs.io/

## How to submit changes

Open a [pull request] to submit changes to this project.

Your pull request needs to meet the following guidelines for acceptance:

- The Nox test suite must pass without errors and warnings.
- Include unit tests. This project maintains 100% code coverage.
- If your changes add functionality, update the documentation accordingly.

Feel free to submit early, though—we can always iterate on this.

To run linting and code formatting checks before committing your change, you can install pre-commit as a Git hook by running the following command:

```console
nox --session=pre-commit -- install
```

It is recommended to open an issue before starting work on anything.
This will allow a chance to talk it over with the owners and validate your approach.

[pull request]: https://github.com/flexion/devops-deployment-metrics/pulls

## Contributors are required to sign commits

GitHub has made it simple for contributors to
[sign commits with their existing SSH keys](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification#ssh-commit-signature-verification).
1Password 8 has [some sugar](https://blog.1password.com/git-commit-signing/) that simplifies this.
Contributors should already be using SSH keys to push to GitHub.

<!-- github-only -->

[code of conduct]: CODE_OF_CONDUCT.md
