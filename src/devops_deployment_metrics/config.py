from dataclasses import dataclass
from typing import Iterator

import toml


@dataclass
class WorkflowConfig:
    owner: str
    repo: str
    id: str
    name: str = None


class Config:
    def __init__(self, config_path: str) -> None:
        self.config = toml.load(config_path)
        self.start_of_time = self.config["general"]["start-date"]
        self.time_slice = self.config["general"]["time-slice-days"]
        self.date_format = self.config["general"]["date-format"]
        self.workflows = self._get_workflows()

    def _get_workflows(self) -> Iterator[WorkflowConfig]:
        for repository in self.config["repositories"]:
            yield WorkflowConfig(
                repository["owner"], repository["repo"], repository["id"]
            )
