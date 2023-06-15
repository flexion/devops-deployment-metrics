"""Utility functions for the devops_deployment_metrics package."""
from typing import Any

from github import Github


def connect_to_github(username: str, password: str) -> Any:
    """Connect to GitHub."""
    return Github(login_or_token=username, password=password, verify=True)
