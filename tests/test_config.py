"""Test the Config class."""
import datetime
import os
import tempfile
from pathlib import Path
from typing import Any

import pytest
import toml
from devops_deployment_metrics.config import Config
from devops_deployment_metrics.config import get_config
from devops_deployment_metrics.workflow import Workflow


@pytest.fixture
def config_data() -> dict[str, Any]:
    """Return a sample configuration file."""
    return {
        "title": "Sample devops-deployment-metrics configuration",
        "general": {
            "time-slice-days": 7,
            "start-date": "2022-06-01T00:01:00",
            "date-format": "%Y-%m-%d",
        },
        "repositories": [
            {
                "owner": "my_github_owner",
                "repo": "my_github_repository",
                "id": "12345678",
                "deployment-frequency": "df",
                "change-fail-rate": "cf",
                "mean-time-to-recover": "mttrs",
                "deployment-log": "deployments",
            },
            {
                "owner": "my_github_owner",
                "repo": "my_other_github_repository",
                "id": "23456789",
                "deployment-frequency": "df",
                "change-fail-rate": "cf",
                "mean-time-to-recover": "mttrs",
                "deployment-log": "deployments",
            },
        ],
    }


@pytest.fixture
def config_path(config_data: dict[str, Any]) -> Any:
    """Create a temporary config file."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write(toml.dumps(config_data))
        file_path = f.name
    yield Path(file_path)
    os.remove(file_path)


def test_config(config_path: Path) -> None:
    """Test the Config class."""
    config = get_config(config_path)

    assert isinstance(config, Config)
    assert config.start_date == datetime.datetime(2022, 6, 1, 0, 1)
    assert config.days_slice == 7
    assert config.date_format == "%Y-%m-%d"
    assert len(config.workflows) == 2

    workflow1, workflow2 = config.workflows

    assert isinstance(workflow1, Workflow)
    assert isinstance(workflow2, Workflow)
