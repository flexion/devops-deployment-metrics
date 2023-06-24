"""Utility functions for the devops_deployment_metrics package."""
from pathlib import Path
from typing import Any

from github import Github


def get_project_root() -> Path:
    """Consistently get the project root for any module in source tree."""
    return Path(__file__).parent.parent.parent


def connect_to_github(username: str, password: str) -> Any:
    """Connect to GitHub."""
    return Github(login_or_token=username, password=password, verify=True)
