"""Command-line interface."""
import logging
import os
import sys
import traceback
from datetime import datetime

import click
import toml
from devops_deployments_metrics.deployments import all_get_mttrs
from devops_deployments_metrics.deployments import collate_mttrs
from devops_deployments_metrics.deployments import (
    get_deployment_frequencies_and_change_failures,
)
from devops_deployments_metrics.deployments import get_deployments
from devops_deployments_metrics.writer import write_csv


@click.command()
@click.version_option()
@click.option("--config", "-c", help="TOML configuration file", type=str)
@click.option(
    "--debug",
    "-d",
    help="Print lots of debugging statements",
    is_flag=True,
    default=False,
)
@click.option("--verbose", "-v", help="Be verbose", is_flag=True, default=False)
@click.option(
    "--username",
    "-u",
    prompt="GitHub user name",
    default=lambda: os.environ.get("GITHUB_USER", ""),
)
@click.option(
    "--password",
    "-p",
    prompt="GitHub token",
    hide_input=True,
    default=lambda: os.environ.get("GITHUB_TOKEN", ""),
)
def main(config: str, verbose, debug, username: str, password: str) -> None:
    """DevOps Deployments Metrics."""

    config = toml.load(config)
    start_of_time = config["general"]["start-date"]
    time_slice = config["general"]["time-slice-days"]
    date_format = config["general"]["date-format"]
    # Set up logger
    if debug:
        loglevel = logging.DEBUG
    elif verbose:
        loglevel = logging.INFO
    else:
        loglevel = logging.WARNING
    logging.basicConfig(
        level=loglevel, filename="gh-deployments.log"
    )  # todo config log filename
    logging.info(f"Starting at {datetime.now()}")
    logging.info(f"GitHub user {username}")

    try:
        all_deployments = []
        for repository in config["repositories"]:
            repo = repository["repo"]
            owner = repository["owner"]
            id = repository["id"]
            deployments = get_deployments(owner, repo, id, username, password)
            all_deployments.extend(deployments)
        (
            deployment_frequencies,
            change_failures,
        ) = get_deployment_frequencies_and_change_failures(
            all_deployments, start_of_time, time_slice
        )
        all_mttrs = all_get_mttrs(all_deployments)
        mttrs = collate_mttrs(all_mttrs, start_of_time, time_slice)
        write_csv(
            deployment_frequencies, "df.csv", date_format
        )  # todo config output filename
        write_csv(change_failures, "cf.csv", date_format)  # todo config filename
        write_csv(mttrs, "mttrs.csv", date_format)  # todo config filename
        result = 1
        if result > 0:
            sys.exit(0)
        else:
            exit(-1)
    except AttributeError as err:
        logging.warning(f"AttributeError: {format(err.message)}")
        # parser.print_help()
    except SystemExit:
        logging.warning("SystemExit")
        raise
    except:  # noqa: E722
        traceback.print_exc()
        logging.warning(f"Exception: {traceback.print_exc()}")
        exit(1)


if __name__ == "__main__":
    main(prog_name="devops-deployments-metrics")  # pragma: no cover
