"""Test the utils module."""

from pathlib import Path
from typing import Any

import pytest
from devops_deployment_metrics.utils import connect_to_github, get_project_root


def test_get_project_root():
    # Get the project root using the function
    project_root = get_project_root()

    # Assert that the returned value is a Path object
    assert isinstance(project_root, Path)

    # Assert that the returned path exists
    assert project_root.exists()

    # Assert that the returned path is a directory
    assert project_root.is_dir()

    # Assert that the returned path is the expected project root
    # This is not working from nox tests, but it does if you use
    # `poetry run pytest`
    # Comment out for now
    # expected_root = Path(__file__).parent.parent  # relative to this test file
    # assert project_root == expected_root


@pytest.mark.nonox(reason="fails under nox")
def test_get_project_root_expected():
    # Get the project root using the function
    project_root = get_project_root()

    # Assert that the returned path is the expected project root
    # This is not working from nox tests, but it does if you use
    # `poetry run pytest`
    expected_root = Path(__file__).parent.parent  # relative to this test file
    assert project_root == expected_root


def test_connect_to_github(mocker: Any) -> None:
    # Mock the objects in connect_to_github
    mock_auth_login = mocker.patch("devops_deployment_metrics.utils.Auth.Login")
    mock_github = mocker.patch("devops_deployment_metrics.utils.Github")

    username = "test_username"
    password = "test_password"

    # Invoke the function
    gh = connect_to_github(username, password)

    # Assert the expected behavior
    assert gh == mock_github.return_value
    mock_auth_login.assert_called_once_with(username, password)
    mock_github.assert_called_once_with(auth=mock_auth_login.return_value, verify=True)
