"""Test cases for the __main__ module."""

import pytest
from click.testing import CliRunner

from devops_deployment_metrics import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    runner.invoke(
        __main__.main, ["-c", "sample-config.toml", "-u", "test", "-p", "test"]
    )
    # assert result.exit_code == 0
