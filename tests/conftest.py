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
