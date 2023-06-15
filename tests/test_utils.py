"""Test the utils module."""
from typing import Any

from devops_deployment_metrics.utils import connect_to_github


def test_connect_to_github(mocker: Any) -> None:
    """Test the connect_to_github function."""
    github_mock = mocker.patch("devops_deployment_metrics.utils.Github")
    gh = connect_to_github("username", "token")
    github_mock.assert_called_once_with(
        login_or_token="username", password="token", verify=True
    )
    assert gh == github_mock.return_value
