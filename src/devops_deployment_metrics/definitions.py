"""Definitions for the DevOps Deployment Metrics package."""
from enum import Enum

from devops_deployment_metrics.utils import get_project_root

ROOT_PATH = get_project_root()

OUTPUT_PATH = ROOT_PATH / "data"
OUTPUT_PATH.mkdir(exist_ok=True)

SAMPLE_CONFIG_PATH = ROOT_PATH / "sample-config.toml"


class MetricName(Enum):
    """An enum for the metric names."""

    DEPLOYMENT_FREQUENCY = "deployment_frequency"
    CHANGE_FAIL_RATE = "change_fail_rate"
    MEAN_TIME_TO_RECOVER = "mean_time_to_recover"
    DEPLOYMENT_LOG = "deployment_log"
