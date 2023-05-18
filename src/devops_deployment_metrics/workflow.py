import datetime
from dataclasses import dataclass

from devops_deployment_metrics.definitions import MetricName
from github import Github


@dataclass
class WorkflowRun:
    id: str
    status: str
    conclusion: str
    run_started: datetime
    run_attempt: int
    created_at: datetime
    updated_at: datetime
    head_branch: str
    url: str


class Workflow:
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
        self.owner = owner
        self.repo = repo
        self.id = id
        self.output = {
            MetricName.DEPLOYMENT_FREQUENCY: deployment_frequency,
            MetricName.CHANGE_FAIL_RATE: change_fail_rate,
            MetricName.MEAN_TIME_TO_RECOVER: mean_time_to_recover,
            MetricName.DEPLOYMENT_LOG: deployment_log,
        }

        self.name = None
        self.runs = []

    @property
    def repo_name(self):
        return f"{self.owner}/{self.repo}"

    def load(self, gh: Github) -> None:
        repo = gh.get_repo(self.repo_name)
        workflow = repo.get_workflow(self.id)
        self.name = workflow.name
        self.runs = [
            WorkflowRun(
                run.id,
                run.status,
                run.conclusion,
                run.run_started_at,
                run.run_attempt,
                run.created_at,
                run.updated_at,
                run.head_branch,
                run.url,
            )
            for run in workflow.get_runs()
        ]
