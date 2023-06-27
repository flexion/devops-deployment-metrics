"""Test the utils module."""
from devops_deployment_metrics.utils import connect_to_github


def test_connect_to_github(mocker) -> None:
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
