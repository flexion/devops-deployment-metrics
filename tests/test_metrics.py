"""Test the metrics module."""

from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pytest

from devops_deployment_metrics.config import Config, get_config
from devops_deployment_metrics.definitions import MetricName
from devops_deployment_metrics.metrics import (
    DeploymentChangeFailRateMetric,
    DeploymentFrequencyMetric,
    DeploymentLogMetric,
    DeploymentMeanTimeToRecoverMetric,
    Metric,
)
from devops_deployment_metrics.workflow import WorkflowRun


@pytest.fixture
def config(config_path: Path) -> Config:
    """Return a Config object."""
    return get_config(config_path)


@pytest.fixture
def deployments() -> list[WorkflowRun]:
    """Return a list of WorkflowRun objects."""
    return [
        WorkflowRun(
            id=1,
            status="completed",
            conclusion="success",
            run_started=datetime(2022, 6, 1, 0, 1, tzinfo=timezone.utc),
            run_attempt=1,
            created_at=datetime(2022, 6, 1, 0, 1, tzinfo=timezone.utc),
            updated_at=datetime(2022, 6, 1, 0, 1, tzinfo=timezone.utc),
            head_branch="main",
            url="https://github.com/test/test/actions/runs/111",
        ),
        WorkflowRun(
            id=2,
            status="completed",
            conclusion="success",
            run_started=datetime(2022, 6, 1, 10, 1, tzinfo=timezone.utc),
            run_attempt=1,
            created_at=datetime(2022, 6, 1, 10, 1, tzinfo=timezone.utc),
            updated_at=datetime(2022, 6, 1, 10, 1, tzinfo=timezone.utc),
            head_branch="main",
            url="https://github.com/test/test/actions/runs/222",
        ),
        WorkflowRun(
            id=3,
            status="completed",
            conclusion="failure",
            run_started=datetime(2022, 6, 3, 0, 1, tzinfo=timezone.utc),
            run_attempt=1,
            created_at=datetime(2022, 6, 3, 0, 1, tzinfo=timezone.utc),
            updated_at=datetime(2022, 6, 3, 0, 1, tzinfo=timezone.utc),
            head_branch="main",
            url="https://github.com/test/test/actions/runs/333",
        ),
        WorkflowRun(
            id=4,
            status="completed",
            conclusion="success",
            run_started=datetime(2022, 6, 4, 0, 1, tzinfo=timezone.utc),
            run_attempt=1,
            created_at=datetime(2022, 6, 4, 0, 1, tzinfo=timezone.utc),
            updated_at=datetime(2022, 6, 4, 0, 1, tzinfo=timezone.utc),
            head_branch="main",
            url="https://github.com/test/test/actions/runs/444",
        ),
        WorkflowRun(
            id=5,
            status="completed",
            conclusion="failure",
            run_started=datetime(2022, 6, 5, 0, 1, tzinfo=timezone.utc),
            run_attempt=1,
            created_at=datetime(2022, 6, 5, 0, 1, tzinfo=timezone.utc),
            updated_at=datetime(2022, 6, 5, 0, 1, tzinfo=timezone.utc),
            head_branch="main",
            url="https://github.com/test/test/actions/runs/555",
        ),
        WorkflowRun(
            id=6,
            status="completed",
            conclusion="success",
            run_started=datetime(2022, 6, 7, 0, 1, tzinfo=timezone.utc),
            run_attempt=1,
            created_at=datetime(2022, 6, 7, 0, 1, tzinfo=timezone.utc),
            updated_at=datetime(2022, 6, 7, 0, 1, tzinfo=timezone.utc),
            head_branch="main",
            url="https://github.com/test/test/actions/runs/666",
        ),
        WorkflowRun(
            id=7,
            status="completed",
            conclusion="failure",
            run_started=datetime(2022, 6, 9, 0, 1, tzinfo=timezone.utc),
            run_attempt=1,
            created_at=datetime(2022, 6, 9, 0, 1, tzinfo=timezone.utc),
            updated_at=datetime(2022, 6, 9, 0, 1, tzinfo=timezone.utc),
            head_branch="main",
            url="https://github.com/test/test/actions/runs/192021",
        ),
        WorkflowRun(
            id=8,
            status="completed",
            conclusion="failure",
            run_started=datetime(2022, 6, 10, 0, 1, tzinfo=timezone.utc),
            run_attempt=1,
            created_at=datetime(2022, 6, 10, 0, 1, tzinfo=timezone.utc),
            updated_at=datetime(2022, 6, 10, 0, 1, tzinfo=timezone.utc),
            head_branch="main",
            url="https://github.com/test/test/actions/runs/192021",
        ),
        WorkflowRun(
            id=9,
            status="completed",
            conclusion="other_conclusion",
            run_started=datetime(2022, 6, 11, 0, 1, tzinfo=timezone.utc),
            run_attempt=1,
            created_at=datetime(2022, 6, 11, 0, 1, tzinfo=timezone.utc),
            updated_at=datetime(2022, 6, 11, 0, 1, tzinfo=timezone.utc),
            head_branch="main",
            url="https://github.com/test/test/actions/runs/888",
        ),
        WorkflowRun(
            id=10,
            status="completed",
            conclusion="failure",
            run_started=datetime(2022, 6, 14, 0, 1, tzinfo=timezone.utc),
            run_attempt=1,
            created_at=datetime(2022, 6, 14, 0, 1, tzinfo=timezone.utc),
            updated_at=datetime(2022, 6, 14, 0, 1, tzinfo=timezone.utc),
            head_branch="main",
            url="https://github.com/test/test/actions/runs/999",
        ),
        WorkflowRun(
            id=11,
            status="completed",
            conclusion="success",
            run_started=datetime(2022, 6, 16, 0, 1, tzinfo=timezone.utc),
            run_attempt=1,
            created_at=datetime(2022, 6, 16, 0, 1, tzinfo=timezone.utc),
            updated_at=datetime(2022, 6, 16, 0, 1, tzinfo=timezone.utc),
            head_branch="main",
            url="https://github.com/test/test/actions/runs/999",
        ),
    ]


def test_metric(config: Config) -> None:
    """Test the Metric class."""
    metric_type = MetricName.DEPLOYMENT_FREQUENCY
    metric = Metric(metric_type, config)
    assert metric.name == metric_type
    assert metric.start_date == datetime(2022, 6, 1, 0, 1, tzinfo=timezone.utc)
    assert metric.days_slice == 7
    assert metric.date_format == "%Y-%m-%d"


def test_get_deployments_in_period(deployments: list[WorkflowRun]) -> None:
    """Test the get_deployments_in_period method."""
    start_date = datetime(2022, 6, 1, 0, 1, tzinfo=timezone.utc)
    end_period = datetime(2022, 6, 15, 0, 1, tzinfo=timezone.utc)
    days_slice = 7
    runs = list(
        Metric.get_deployments_in_period(
            deployments, days_slice, start_date, end_period
        )
    )

    assert len(runs) == 3

    run1_start_date, run1_deployments = runs[0]
    assert run1_start_date == datetime(2022, 6, 1, 0, 1, tzinfo=timezone.utc)
    assert len(run1_deployments) == 6
    assert run1_deployments[0].id == 1

    run2_start_date, run2_deployments = runs[1]
    assert run2_start_date == datetime(2022, 6, 8, 0, 1, tzinfo=timezone.utc)
    assert len(run2_deployments) == 4
    assert run2_deployments[0].id == 7

    run3_start_date, run3_deployments = runs[2]
    assert run3_start_date == datetime(2022, 6, 15, 0, 1, tzinfo=timezone.utc)
    assert len(run3_deployments) == 1
    assert run3_deployments[0].id == 11


def test_deployment_frequency_metric(
    benchmark: Any, config: Config, deployments: list[WorkflowRun]
) -> None:
    """Test the DeploymentFrequencyMetric class."""
    metric = DeploymentFrequencyMetric(config)
    assert metric.name == MetricName.DEPLOYMENT_FREQUENCY

    results = benchmark(metric.calculate, deployments)

    assert results[0]["date"] == datetime(2022, 6, 1, 0, 1, tzinfo=timezone.utc)
    assert round(results[0]["frequency"], 2) == 0.57
    assert results[0]["count"] == 4

    assert results[1]["date"] == datetime(2022, 6, 8, 0, 1, tzinfo=timezone.utc)
    assert round(results[1]["frequency"], 2) == 0
    assert results[1]["count"] == 0

    assert results[2]["date"] == datetime(2022, 6, 15, 0, 1, tzinfo=timezone.utc)
    assert round(results[2]["frequency"], 2) == 0.14
    assert results[2]["count"] == 1


def test_change_fail_rate_metric(
    benchmark: Any, config: Config, deployments: list[WorkflowRun]
) -> None:
    """Test the DeploymentChangeFailRateMetric class."""
    metric = DeploymentChangeFailRateMetric(config)
    assert metric.name == MetricName.CHANGE_FAIL_RATE

    results = benchmark(metric.calculate, deployments)

    assert results[0]["date"] == datetime(2022, 6, 1, 0, 1, tzinfo=timezone.utc)
    assert round(results[0]["percent"], 2) == 33.33

    assert results[1]["date"] == datetime(2022, 6, 8, 0, 1, tzinfo=timezone.utc)
    assert round(results[1]["percent"], 2) == 75.0

    assert results[2]["date"] == datetime(2022, 6, 15, 0, 1, tzinfo=timezone.utc)
    assert round(results[2]["percent"], 2) == 0.0


def test_mean_time_to_recovery_metric(
    benchmark: Any, config: Config, deployments: list[WorkflowRun]
) -> None:
    """Test the DeploymentMeanTimeToRecoverMetric class."""
    metric = DeploymentMeanTimeToRecoverMetric(config)
    assert metric.name == MetricName.MEAN_TIME_TO_RECOVER

    results = benchmark(metric.calculate, deployments)

    assert results[0]["date"] == datetime(2022, 6, 1, 0, 1, tzinfo=timezone.utc)
    assert round(results[0]["mttr"], 2) == 36.0

    assert results[1]["date"] == datetime(2022, 6, 8, 0, 1, tzinfo=timezone.utc)
    assert round(results[1]["mttr"], 2) == 0.0

    assert results[2]["date"] == datetime(2022, 6, 15, 0, 1, tzinfo=timezone.utc)
    assert round(results[2]["mttr"], 2) == 168.0


def test_deployment_log(config: Config, deployments: list[WorkflowRun]) -> None:
    """Test the DeploymentLogMetric class."""
    metric = DeploymentLogMetric(config)
    assert metric.name == MetricName.DEPLOYMENT_LOG

    results = metric.calculate(deployments)

    for i, result in enumerate(results):
        assert result == asdict(deployments[i])
