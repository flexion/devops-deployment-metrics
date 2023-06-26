"""Utility functions for the devops_deployment_metrics package."""
from typing import Any

from github import Auth
from github import Github


def connect_to_github(username: str, password: str) -> Any:
    """Connect to GitHub."""
    # Create an instance of the Auth.Login class with your GitHub credentials
    auth = Auth.Login("username", "password")

    # Create a GitHub instance with the authentication
    return Github(auth=auth, verify=True)
