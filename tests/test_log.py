"""Test cases for the __main__ module."""
import logging
import os
from unittest.mock import Mock

import pytest
from devops_deployment_metrics.definitions import ROOT_PATH
from devops_deployment_metrics.log import get_logger
from devops_deployment_metrics.log import set_console_level
from devops_deployment_metrics.log import setup_logging


@pytest.fixture(scope="function")
def mock_logging_config(tmp_path):
    log_dir = tmp_path
    log_dir.mkdir(exist_ok=True)

    config = {
        "version": 1,
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "stream": "ext://sys.stdout",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "WARNING",
        },
    }

    with open(log_dir / "logging.yaml", "w") as f:
        f.write(str(config))

    return config


def test_setup_logging(mock_logging_config, tmp_path):
    """Test logging setup with scratch config."""
    setup_logging(verbose=False, debug=False, root_path=tmp_path)

    assert os.path.exists(tmp_path / "logging.yaml")
    assert os.path.exists(tmp_path / "logs")
    assert len(logging.getLogger().handlers) == 1

    console_handler = logging.getLogger().handlers[0]
    assert isinstance(console_handler, logging.StreamHandler)
    assert console_handler.level == logging.WARNING


def test_setup_logging_repro_yaml():
    """Test logging setup with config from repro."""
    setup_logging(verbose=False, debug=False)

    assert os.path.exists(ROOT_PATH / "logs")
    assert os.path.exists(ROOT_PATH / "logging.yaml")
    assert len(logging.getLogger().handlers) == 2

    console_handler = logging.getLogger().handlers[1]
    assert isinstance(console_handler, logging.FileHandler)
    assert console_handler.level == logging.DEBUG


def test_set_console_level():
    mock_console_handler = Mock(spec=logging.StreamHandler)
    mock_console_handler.setLevel = Mock()

    logger = logging.getLogger()
    logger.handlers = [mock_console_handler]

    set_console_level(verbose=True, debug=False)
    mock_console_handler.setLevel.assert_called_once_with(logging.INFO)


def test_set_console_level_debug():
    mock_console_handler = Mock(spec=logging.StreamHandler)
    mock_console_handler.setLevel = Mock()

    logger = logging.getLogger()
    logger.handlers = [mock_console_handler]

    set_console_level(verbose=False, debug=True)
    mock_console_handler.setLevel.assert_called_once_with(logging.DEBUG)


def test_set_console_level_default():
    mock_console_handler = Mock(spec=logging.StreamHandler)
    mock_console_handler.setLevel = Mock()

    logger = logging.getLogger()
    logger.handlers = [mock_console_handler]

    set_console_level(verbose=False, debug=False)
    mock_console_handler.setLevel.assert_called_once_with(logging.WARNING)


def test_get_logger():
    logger = get_logger("test_logger")
    assert isinstance(logger, logging.Logger)
    assert logger.name == "test_logger"
