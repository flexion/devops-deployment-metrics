"""This module contains classes for calculating deployment metrics."""
from dataclasses import asdict
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import Any
from typing import Iterable
from typing import Optional

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

    def save(self) -> None:
        """Save the metric output to a CSV file."""
        for name, deployments in self.output.items():
            file_name = f"{name}.csv"
            results = self.calculate(deployments)
            df = pd.DataFrame.from_dict(results)  # type: ignore
            df.to_csv(
                OUTPUT_PATH / file_name, index=False, date_format=self.date_format
            )

    @staticmethod
    def get_deployments_in_period(
        deployments: list[WorkflowRun],
        days_slice: int,
        start_date: datetime,
        end_period: Optional[datetime] = None,
    ) -> Iterable[tuple[datetime, list[WorkflowRun]]]:
        """Get the deployments for each period."""
        # Using this workaround to get the current datetime with the local timezone
        now = datetime.now(timezone.utc).astimezone()
        end_period = end_period or now
        end_date = start_date + timedelta(days=days_slice)

        while start_date <= end_period:
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
            end_date = start_date + timedelta(days=days_slice)


class DeploymentFrequencyMetric(Metric):
    """A class for calculating the deployment frequency metric."""

    def __init__(self, config: Config) -> None:
        """Initialize a new DeploymentFrequencyMetric object."""
        super().__init__(MetricName.DEPLOYMENT_FREQUENCY, config)

    def calculate(self, deployments: list[WorkflowRun]) -> list[dict[str, Any]]:
        """Calculate the deployment frequency metric."""
        deployments_in_period = self.get_deployments_in_period(
            deployments, self.days_slice, self.start_date
        )
        results = []
        for start_date, deployments in deployments_in_period:
            successful_deployments = [
                d for d in deployments if d.conclusion == "success"
            ]
            count = len(successful_deployments)
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
        deployments_in_period = self.get_deployments_in_period(
            deployments, self.days_slice, self.start_date
        )
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


class DeploymentMeanTimeToRecoverMetric(Metric):
    """A class for calculating the mean time to recover metric."""

    def __init__(self, config: Config) -> None:
        """Initialize a new DeploymentMeanTimeToRecoverMetric object."""
        super().__init__(MetricName.MEAN_TIME_TO_RECOVER, config)

    def calculate(self, deployments: list[WorkflowRun]) -> list[dict[str, Any]]:
        """Calculate the mean time to recover metric."""
        results = []
        start_recovery = None
        deployments_in_period = self.get_deployments_in_period(
            deployments, self.days_slice, self.start_date
        )
        for start_date, deployments in deployments_in_period:
            deployments.sort(key=lambda x: x.run_started)
            recovery_times = []
            for deployment in deployments:
                if deployment.conclusion == "failure" and not start_recovery:
                    start_recovery = deployment.run_started
                elif start_recovery and deployment.conclusion == "success":
                    recovery_time = (
                        deployment.run_started - start_recovery
                    ).total_seconds() / 3600
                    recovery_times.append(recovery_time)
                    start_recovery = None
            if recovery_times:
                mean_time_to_recover = sum(recovery_times) / len(recovery_times)
            else:
                mean_time_to_recover = 0
            results.append({"date": start_date, "mttr": mean_time_to_recover})
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
        DeploymentMeanTimeToRecoverMetric(config),
        DeploymentLogMetric(config),
    ]
