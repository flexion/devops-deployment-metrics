"""Pytest configuration file."""
import os
import tempfile
from pathlib import Path
from typing import Any

import pytest


@pytest.fixture
def config_data() -> str:
    """Return a sample configuration file."""
    return """
title = "Sample devops-deployment-metrics configuration"

[general]
    time-slice-days = 7
    start-date = 2022-06-01T00:01:00
    date-format = "%Y-%m-%d"

[[repositories]]
    owner = "my_github_owner"
    repo = "my_github_repository"
    id = "12345678"
    deployment-frequency = "df"
    change-fail-rate = "cf"
    mean-time-to-recover = "mttrs"
    deployment-log = "deployments"

[[repositories]]
    owner = "my_github_owner"
    repo = "my_other_github_repository"
    id = "23456789"
    deployment-frequency = "df"
    change-fail-rate = "cf"
    mean-time-to-recover = "mttrs"
    deployment-log = "deployments"
    """


@pytest.fixture
def config_path(config_data: str) -> Any:
    """Create a temporary config file."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write(config_data)
        file_path = f.name
    yield Path(file_path)
    os.remove(file_path)


# Implement command line skipping of tests when running nox.
# Tests that work when run from the project root will not behave when run
# in a nox session, which is running from some other directory down
# the nox path.
# Hack - configure nox to call pytests with the --no-nox argument
# then implement the following to skip tests marked `no-nox`.
#
# See https://docs.pytest.org/en/latest/example/simple.html#control-skipping-of-tests-according-to-command-line-option


def pytest_addoption(parser):
    parser.addoption(
        "--no-nox",
        action="store_true",
        default=False,
        help="Skip tests nox can run correctly.",
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "nonox: mark test as won't run under nox")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--no-nox"):
        skip_no_nox = pytest.mark.skip(reason="need no --no-nox option to run")
        for item in items:
            if "nonox" in item.keywords:
                item.add_marker(skip_no_nox)
