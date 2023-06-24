"""Logging configuration and utilities."""
import logging.config
import os
from pathlib import PosixPath

import yaml

from .definitions import ROOT_PATH


def setup_logging(verbose: bool, debug: bool, root_path: PosixPath = ROOT_PATH) -> None:
    """Setup logging configuration."""
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
