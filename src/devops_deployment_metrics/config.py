from dataclasses import dataclass
from datetime import datetime

import toml
from devops_deployment_metrics.workflow import Workflow


@dataclass
class Config:
    start_date: datetime
    days_slice: int
    date_format: str
    workflows: list[Workflow]


def get_config(config_path: str) -> Config:
    cfg = toml.load(config_path)
    wdefs = [
        Workflow(
            wf["owner"],
            wf["repo"],
            wf["id"],
            wf["deployment-frequency"],
            wf["change-fail-rate"],
            wf["mean-time-to-recover"],
            wf["deployment-log"],
        )
        for wf in cfg["repositories"]
    ]
    return Config(
        cfg["general"]["start-date"],
        cfg["general"]["time-slice-days"],
        cfg["general"]["date-format"],
        wdefs,
    )
