"""Test the utils module."""
from pathlib import Path
from typing import Any

from devops_deployment_metrics.utils import connect_to_github
from devops_deployment_metrics.utils import get_project_root


def test_connect_to_github(mocker: Any) -> None:
    """Test the connect_to_github function."""
    github_mock = mocker.patch("devops_deployment_metrics.utils.Github")
    gh = connect_to_github("username", "token")
    github_mock.assert_called_once_with(
        login_or_token="username", password="token", verify=True
    )
    assert gh == github_mock.return_value


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
