# Contributing to devops-deployment-metrics

## Contributors are required to sign commits

GitHub has of late made it very simple for contributors to
[sign commits with their existing SSH keys](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification#ssh-commit-signature-verification).
1Password 8 has [some sugar](https://blog.1password.com/git-commit-signing/) that simplifies this.
Contributors should already be using SSH keys to push to GitHub.

## Setting up development environment

If you're interested in contributing code, you can start by checking out this repository
[https://github.com/flexion/devops-deployment-metrics](https://github.com/flexion/devops-deployment-metrics).
Take a look through the issues and see if there are any tasks you are interested in working on.
Indicate you are working on a task by adding your GitHub @name after the task in the issue.
Definition of Done items are often a great starting point for contributing in a meaningful way while getting integrated into team practices.
Using SSH keys to check out the repository is ideal, as we require contributors to sign their commits.

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
