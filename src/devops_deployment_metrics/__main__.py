"""Command-line interface."""
import click
from devops_deployment_metrics.config import get_config
from devops_deployment_metrics.log import get_logger
from devops_deployment_metrics.log import setup_logging
from devops_deployment_metrics.metrics import get_metrics
from devops_deployment_metrics.utils import connect_to_github
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
    """Devops deployments metrics."""
    setup_logging(verbose, debug)
    logger = get_logger("main")

    logger.info("Reading configuration file")
    cfg = get_config(config)

    logger.info("Connecting to github")
    gh = connect_to_github(username, password)

    logger.info("Getting workflows")
    workflows = cfg.workflows
    metrics = get_metrics(cfg)
    for wf in workflows:
        logger.info(f"Getting deployments for workflow id {wf.id}")
        wf.load(gh)
        for m in metrics:
            m.set_output(wf.output[m.name], wf.runs)

    logger.info("Calculating and saving metrics")
    for m in metrics:
        m.save()


if __name__ == "__main__":
    main(prog_name="devops-deployment-metrics")  # pragma: no cover
