"""Utility functions for the devops_deployment_metrics package."""

from pathlib import Path
from typing import Any

from github import Auth, Github


def get_project_root() -> Path:
    """Consistently get the project root for any module in source tree."""
    return Path(__file__).parent.parent.parent


def connect_to_github(username: str, password: str) -> Any:
    """Connect to GitHub."""
    # Create an instance of the Auth.Login class with your GitHub credentials
    auth = Auth.Login(username, password)

    # Create a GitHub instance with the authentication
    return Github(auth=auth, verify=True)
