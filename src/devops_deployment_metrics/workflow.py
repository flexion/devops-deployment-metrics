"""This module contains classes for working with GitHub Actions workflows."""
from dataclasses import dataclass
from datetime import datetime

from devops_deployment_metrics.definitions import MetricName
from github import Github
from tqdm import tqdm


@dataclass
class WorkflowRun:
    """Shell for GitHub workflow run."""

    id: int
    status: str
    conclusion: str
    run_started: datetime
    run_attempt: int
    created_at: datetime
    updated_at: datetime
    head_branch: str
    url: str


class Workflow:
    """Shell for a GitHub workflow."""

    def __init__(
        self,
        owner: str,
        repo: str,
        id: str,
        deployment_frequency: str,
        change_fail_rate: str,
        mean_time_to_recover: str,
        deployment_log: str,
    ) -> None:
        """Initializes a Workflow object."""
        self.owner = owner
        self.repo = repo
        self.id = id
        self.output = {
            MetricName.DEPLOYMENT_FREQUENCY: deployment_frequency,
            MetricName.CHANGE_FAIL_RATE: change_fail_rate,
            MetricName.MEAN_TIME_TO_RECOVER: mean_time_to_recover,
            MetricName.DEPLOYMENT_LOG: deployment_log,
        }

        self.name = ""
        self.runs: list[WorkflowRun] = []

    @property
    def repo_name(self) -> str:
        """Returns the name of the repository."""
        return f"{self.owner}/{self.repo}"

    def load(self, gh: Github) -> None:
        """Loads the workflow runs from GitHub."""
        repo = gh.get_repo(self.repo_name)
        workflow = repo.get_workflow(self.id)
        workflow_runs = workflow.get_runs()
        self.name = workflow.name
        self.runs = [
            WorkflowRun(
                run.id,
                run.status,
                run.conclusion,
                run.run_started_at,  # type: ignore
                run.run_attempt,
                run.created_at,
                run.updated_at,
                run.head_branch,
                run.url,
            )
            for run in tqdm(workflow_runs)
        ]
