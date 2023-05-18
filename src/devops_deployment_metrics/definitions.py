from enum import Enum
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent.parent

OUTPUT_PATH = ROOT_PATH / "data"
OUTPUT_PATH.mkdir(exist_ok=True)


class MetricName(Enum):
    DEPLOYMENT_FREQUENCY = "deployment_frequency"
    CHANGE_FAIL_RATE = "change_fail_rate"
    MEAN_TIME_TO_RECOVER = "mean_time_to_recover"
    DEPLOYMENT_LOG = "deployment_log"