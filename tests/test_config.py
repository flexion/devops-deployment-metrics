"""Test the Config class."""
import datetime

from devops_deployment_metrics.config import Config
from devops_deployment_metrics.config import get_config
from devops_deployment_metrics.definitions import SAMPLE_CONFIG_PATH
from devops_deployment_metrics.workflow import Workflow


def test_config() -> None:
    """Test the Config class."""
    config = get_config(SAMPLE_CONFIG_PATH)

    assert isinstance(config, Config)
    assert config.start_date == datetime.datetime(2022, 6, 1, 0, 1)
    assert config.days_slice == 7
    assert config.date_format == "%Y-%m-%d"
    assert len(config.workflows) == 2

    workflow1, workflow2 = config.workflows

    assert isinstance(workflow1, Workflow)
    assert isinstance(workflow2, Workflow)
