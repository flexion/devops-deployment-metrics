"""Test the utils module."""
from unittest.mock import MagicMock
from unittest.mock import patch

from devops_deployment_metrics.utils import connect_to_github


def test_connect_to_github() -> None:
    # Mock the necessary objects
    mock_auth = MagicMock()
    mock_github = MagicMock()

    # Patch the required classes and methods
    with patch(
        "devops_deployment_metrics.utils.Auth.Login", return_value=mock_auth
    ) as mock_login, patch(
        "devops_deployment_metrics.utils.Github", return_value=mock_github
    ) as mock_github_class:
        username = "test_username"
        password = "test_password"
        # Invoke the function
        gh = connect_to_github(username, password)

        # Assert the expected behavior
        assert gh == mock_github
        mock_login.assert_called_once_with(username, password)
        mock_github_class.assert_called_once_with(auth=mock_auth, verify=True)
