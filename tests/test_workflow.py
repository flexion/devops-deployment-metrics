"""Test the Workflow class."""

from datetime import datetime
from unittest.mock import Mock

import pytest
from devops_deployment_metrics.definitions import MetricName
from devops_deployment_metrics.workflow import Workflow
from github import Github


@pytest.fixture
def mock_gh():
    return Mock(spec=Github)


def test_workflow() -> None:
    """Test the Workflow class."""
    owner = "test-owner"
    repo = "test-repo"
    workflow_filename = "test-filename"
    deployment_frequency = "df"
    change_fail_rate = "cf"
    mean_time_to_recover = "mttrs"
    deployment_log = "deployments"

    workflow = Workflow(
        owner,
        repo,
        workflow_filename,
        deployment_frequency,
        change_fail_rate,
        mean_time_to_recover,
        deployment_log,
    )

    assert workflow.owner == owner
    assert workflow.repo == repo
    assert workflow.workflow_filename == workflow_filename
    assert workflow.repo_name == f"{owner}/{repo}"

    assert isinstance(workflow.output, dict)
    assert workflow.output[MetricName.DEPLOYMENT_FREQUENCY] == deployment_frequency
    assert workflow.output[MetricName.CHANGE_FAIL_RATE] == change_fail_rate
    assert workflow.output[MetricName.MEAN_TIME_TO_RECOVER] == mean_time_to_recover
    assert workflow.output[MetricName.DEPLOYMENT_LOG] == deployment_log


def test_workflow_load(mock_gh):
    """Test the Workflow load method."""
    mock_workflow = Mock()
    mock_workflow.name = "test_workflow"
    mock_workflow_run1 = Mock()
    mock_workflow_run1.id = 1
    mock_workflow_run1.status = "in_progress"
    mock_workflow_run1.conclusion = None
    mock_workflow_run1.run_started_at = datetime.now()
    mock_workflow_run1.run_attempt = 1
    mock_workflow_run1.created_at = datetime.now()
    mock_workflow_run1.updated_at = datetime.now()
    mock_workflow_run1.head_branch = "main"
    mock_workflow_run1.url = "https://github.com/test_owner/test_repo/actions/runs/1"
    mock_workflow_run2 = Mock()
    mock_workflow_run2.id = 2
    mock_workflow_run2.status = "completed"
    mock_workflow_run2.conclusion = "success"
    mock_workflow_run2.run_started_at = datetime.now()
    mock_workflow_run2.run_attempt = 1
    mock_workflow_run2.created_at = datetime.now()
    mock_workflow_run2.updated_at = datetime.now()
    mock_workflow_run2.head_branch = "develop"
    mock_workflow_run2.url = "https://github.com/test_owner/test_repo/actions/runs/2"

    mock_workflow.get_runs.return_value = [
        mock_workflow_run1,
        mock_workflow_run2,
    ]
    mock_repo = Mock()
    mock_repo.get_workflow.return_value = mock_workflow
    mock_gh.get_repo.return_value = mock_repo

    workflow = Workflow(
        owner="test_owner",
        repo="test_repo",
        workflow_filename="test_workflow_file.yaml",
        deployment_frequency="df",
        change_fail_rate="cfr",
        mean_time_to_recover="mttr",
        deployment_log="logs",
    )

    workflow.load(mock_gh)

    assert workflow.name == "test_workflow"
    assert len(workflow.runs) == 2
    assert workflow.runs[0].id == 1
    assert workflow.runs[0].status == "in_progress"
    assert workflow.runs[0].conclusion is None
    assert workflow.runs[0].head_branch == "main"
    assert (
        workflow.runs[0].url == "https://github.com/test_owner/test_repo/actions/runs/1"
    )
    assert workflow.runs[1].id == 2
    assert workflow.runs[1].status == "completed"
    assert workflow.runs[1].conclusion == "success"
    assert workflow.runs[1].head_branch == "develop"
    assert (
        workflow.runs[1].url == "https://github.com/test_owner/test_repo/actions/runs/2"
    )
