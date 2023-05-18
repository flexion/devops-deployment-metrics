from datetime import datetime
from datetime import timedelta
from typing import Iterable

import pandas as pd
from devops_deployment_metrics.config import Config
from devops_deployment_metrics.definitions import MetricName
from devops_deployment_metrics.definitions import OUTPUT_PATH
from devops_deployment_metrics.workflow import WorkflowRun


class Metric:
    def __init__(self, name: str, config: Config) -> None:
        self.name = name
        self.start_date = config.start_date
        self.days_slice = config.days_slice
        self.date_format = config.date_format
        self.output = {}

    def set_output(self, name: str, deployments) -> None:
        self.output.setdefault(name, []).extend(deployments)

    def calculate(self, deployments: list[WorkflowRun]) -> list[any]:
        pass

    def get_deployments_in_period(
        self, deployments: list[WorkflowRun]
    ) -> Iterable[dict[datetime]]:
        start_date = self.start_date
        end_date = start_date + timedelta(days=self.days_slice)
        today = datetime.now()

        while end_date <= today:
            yield (
                start_date,
                [
                    deployment
                    for deployment in deployments
                    if start_date <= deployment.run_started < end_date
                ],
            )

            # Move on to the next period
            start_date = end_date
            end_date = start_date + timedelta(days=self.days_slice)

    def save(self) -> None:
        for name, deployments in self.output.items():
            file_name = f"{name}.csv"
            results = self.calculate(deployments)
            df = pd.DataFrame.from_dict(results)
            df.to_csv(
                OUTPUT_PATH / file_name, index=False, date_format=self.date_format
            )


class DeploymentFrequencyMetric(Metric):
    def __init__(self, config: Config) -> None:
        super().__init__(MetricName.DEPLOYMENT_FREQUENCY, config)

    def calculate(self, deployments: list[WorkflowRun]) -> Iterable[dict]:
        deployments_in_period = self.get_deployments_in_period(deployments)
        for start_date, deployments in deployments_in_period:
            count = len(deployments)
            yield {
                "date": start_date,
                "frequency": count / self.days_slice,
                "count": count,
            }


class DeploymentChangeFailRateMetric(Metric):
    def __init__(self, config: Config) -> None:
        super().__init__(MetricName.CHANGE_FAIL_RATE, config)

    def calculate(self, deployments) -> Iterable[dict]:
        deployments_in_period = self.get_deployments_in_period(deployments)
        for start_date, deployments in deployments_in_period:
            count_total = len(deployments)
            failed_deployments = [
                deployment
                for deployment in deployments
                if deployment.conclusion == "failure"
            ]
            failure_percent = (
                (len(failed_deployments) / count_total * 100.0) if count_total else 0
            )
            yield {"date": start_date, "percent": failure_percent}


class DeploymentLogMetric(Metric):
    def __init__(self, config: Config) -> None:
        super().__init__(MetricName.DEPLOYMENT_LOG, config)
        self.date_format = "%Y-%m-%d %H:%M:%S"

    def calculate(self, deployments) -> list[any]:
        return deployments


def get_metrics(config: Config) -> list[Metric]:
    return [
        DeploymentFrequencyMetric(config),
        DeploymentChangeFailRateMetric(config),
        DeploymentLogMetric(config),
    ]
