"""Test the Workflow class."""
import pytest
from devops_deployment_metrics.definitions import MetricName
from devops_deployment_metrics.workflow import Workflow


def test_workflow() -> None:
    """Test the Workflow class."""
    owner = "test-owner"
    repo = "test-repo"
    id = "test-id"
    deployment_frequency = "df"
    change_fail_rate = "cf"
    mean_time_to_recover = "mttrs"
    deployment_log = "deployments"

    workflow = Workflow(
        owner,
        repo,
        id,
        deployment_frequency,
        change_fail_rate,
        mean_time_to_recover,
        deployment_log,
    )

    assert workflow.owner == owner
    assert workflow.repo == repo
    assert workflow.id == id
    assert workflow.repo_name == f"{owner}/{repo}"

    assert isinstance(workflow.output, dict)
    assert workflow.output[MetricName.DEPLOYMENT_FREQUENCY] == deployment_frequency
    assert workflow.output[MetricName.CHANGE_FAIL_RATE] == change_fail_rate
    assert workflow.output[MetricName.MEAN_TIME_TO_RECOVER] == mean_time_to_recover
    assert workflow.output[MetricName.DEPLOYMENT_LOG] == deployment_log


@pytest.mark.skip(reason="pending")
def test_workflow_load() -> None:
    """Test the Workflow load method."""
    pass
