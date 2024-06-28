"""This module contains classes and functions for working with configuration files."""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import toml
from zoneinfo import ZoneInfo

from devops_deployment_metrics.workflow import Workflow


@dataclass
class Config:
    """A dataclass representing the configuration for the deployment metrics tool."""

    start_date: datetime
    days_slice: int
    date_format: str
    workflows: list[Workflow]


def get_config(config_path: Path) -> Config:
    """Load a configuration file."""
    cfg = toml.load(config_path)
    wdefs = [
        Workflow(
            wf["owner"],
            wf["repo"],
            wf["workflow_filename"],
            wf["deployment-frequency"],
            wf["change-fail-rate"],
            wf["mean-time-to-recover"],
            wf["deployment-log"],
        )
        for wf in cfg["repositories"]
    ]
    timezone = (
        ZoneInfo(cfg["general"]["timezone"])
        if "timezone" in cfg["general"]
        else ZoneInfo("UTC")
    )
    start_date = cfg["general"]["start-date"].replace(tzinfo=timezone)
    return Config(
        start_date,
        cfg["general"]["time-slice-days"],
        cfg["general"]["date-format"],
        wdefs,
    )
