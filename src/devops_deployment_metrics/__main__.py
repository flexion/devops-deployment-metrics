"""Command-line interface."""
from datetime import datetime

import click
from devops_deployment_metrics.config import Config
from devops_deployment_metrics.deployments import all_get_mttrs
from devops_deployment_metrics.deployments import collate_mttrs
from devops_deployment_metrics.deployments import (
    get_deployment_frequencies_and_change_failures,
)
from devops_deployment_metrics.deployments import get_deployments
from devops_deployment_metrics.log import get_logger
from devops_deployment_metrics.log import setup_logging
from devops_deployment_metrics.utils import connect_to_github
from devops_deployment_metrics.writer import write_csv
from dotenv import load_dotenv


load_dotenv()


@click.command()
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
    envvar="GITHUB_USERNAME",
    help="GitHub user name",
)
@click.option(
    "--password",
    "-p",
    prompt="GitHub token",
    hide_input=True,
    envvar="GITHUB_TOKEN",
    help="GitHub token",
)
def main(config: str, verbose: bool, debug: bool, username: str, password: str) -> None:
    """DevOps Deployments Metrics."""

    setup_logging(verbose, debug)
    logger = get_logger("main")
    config = Config(config)

    logger.info(f"Starting at {datetime.now()}")

    start_of_time, time_slice, date_format, logging = None
    gh = connect_to_github(username, password)
    logger.info(gh.get_user().name)
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
    write_csv(all_deployments, "deployments.csv", date_format)  # todo config filename


if __name__ == "__main__":
    main(prog_name="devops-deployment-metrics")  # pragma: no cover
