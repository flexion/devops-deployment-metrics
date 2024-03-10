"""Logging configuration and utilities."""

import logging.config
import os

import yaml

from devops_deployment_metrics.definitions import get_project_root


def setup_logging(verbose: bool, debug: bool) -> None:
    """Setup logging configuration."""
    root_path = get_project_root()
    os.makedirs(f"{root_path}/logs", exist_ok=True)
    with open(f"{root_path}/logging.yaml") as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    set_console_level(verbose, debug)


def set_console_level(verbose: bool, debug: bool) -> None:
    """Set the console log level."""
    if debug:
        loglevel = logging.DEBUG
    elif verbose:
        loglevel = logging.INFO
    else:
        loglevel = logging.WARNING

    console_handler = next(
        handler
        for handler in logging.getLogger().handlers
        if isinstance(handler, logging.StreamHandler)
    )
    console_handler.setLevel(loglevel)


def get_logger(name: str) -> logging.Logger:
    """Get a logger."""
    return logging.getLogger(name)
