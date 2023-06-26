"""Test cases for the __main__ module."""
import logging
import os
from unittest.mock import Mock

import pytest
from devops_deployment_metrics.log import get_logger
from devops_deployment_metrics.log import ROOT_PATH
from devops_deployment_metrics.log import set_console_level
from devops_deployment_metrics.log import setup_logging


@pytest.mark.nonox(reason="fails under nox")
def test_setup_logging_repro_yaml():
    """Test logging setup with test config from repro."""
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
