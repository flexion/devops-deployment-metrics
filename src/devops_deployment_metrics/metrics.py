"""This module contains classes for calculating deployment metrics."""
from dataclasses import asdict
from datetime import datetime
from datetime import timedelta
from typing import Any
from typing import Iterable

import pandas as pd
from devops_deployment_metrics.config import Config
from devops_deployment_metrics.definitions import MetricName
from devops_deployment_metrics.definitions import OUTPUT_PATH
from devops_deployment_metrics.workflow import WorkflowRun


class Metric:
    """A base class for deployment metrics."""

    def __init__(self, name: MetricName, config: Config) -> None:
        """Initialize a new Metric object."""
        self.name = name
        self.start_date = config.start_date
        self.days_slice = config.days_slice
        self.date_format = config.date_format
        self.output: dict[str, list[WorkflowRun]] = {}

    def set_output(self, name: str, deployments: list[WorkflowRun]) -> None:
        """Sets the output for a given metric."""
        self.output.setdefault(name, []).extend(deployments)

    def calculate(self, deployments: list[WorkflowRun]) -> list[dict[str, Any]]:  # type: ignore
        """Calculate the deployment metric."""
        pass

    def get_deployments_in_period(
        self, deployments: list[WorkflowRun]
    ) -> Iterable[tuple[datetime, list[WorkflowRun]]]:
        """Get the deployments for each period."""
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
        """Save the metric output to a CSV file."""
        for name, deployments in self.output.items():
            file_name = f"{name}.csv"
            results = self.calculate(deployments)
            df = pd.DataFrame.from_dict(results)
            df.to_csv(
                OUTPUT_PATH / file_name, index=False, date_format=self.date_format
            )


class DeploymentFrequencyMetric(Metric):
    """A class for calculating the deployment frequency metric."""

    def __init__(self, config: Config) -> None:
        """Initialize a new DeploymentFrequencyMetric object."""
        super().__init__(MetricName.DEPLOYMENT_FREQUENCY, config)

    def calculate(self, deployments: list[WorkflowRun]) -> list[dict[str, Any]]:
        """Calculate the deployment frequency metric."""
        deployments_in_period = self.get_deployments_in_period(deployments)
        results = []
        for start_date, deployments in deployments_in_period:
            count = len(deployments)
            results.append(
                {
                    "date": start_date,
                    "frequency": count / self.days_slice,
                    "count": count,
                }
            )
        return results


class DeploymentChangeFailRateMetric(Metric):
    """A class for calculating the change fail rate metric."""

    def __init__(self, config: Config) -> None:
        """Initialize a new DeploymentChangeFailRateMetric object."""
        super().__init__(MetricName.CHANGE_FAIL_RATE, config)

    def calculate(self, deployments: list[WorkflowRun]) -> list[dict[str, Any]]:
        """Calculate the change fail rate metric."""
        deployments_in_period = self.get_deployments_in_period(deployments)
        results = []
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
            results.append({"date": start_date, "percent": failure_percent})
        return results


class DeploymentLogMetric(Metric):
    """A class to get the deployment log metric."""

    def __init__(self, config: Config) -> None:
        """Initialize a new DeploymentLogMetric object."""
        super().__init__(MetricName.DEPLOYMENT_LOG, config)
        self.date_format = "%Y-%m-%d %H:%M:%S"

    def calculate(self, deployments: list[WorkflowRun]) -> list[dict[str, Any]]:
        """Get the deployment log metric."""
        return [asdict(wf) for wf in deployments]


def get_metrics(config: Config) -> list[Metric]:
    """Get a list of metrics to calculate."""
    return [
        DeploymentFrequencyMetric(config),
        DeploymentChangeFailRateMetric(config),
        DeploymentLogMetric(config),
    ]
