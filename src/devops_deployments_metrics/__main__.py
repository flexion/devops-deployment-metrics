"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """DevOps Deployments Metrics."""


if __name__ == "__main__":
    main(prog_name="devops-deployments-metrics")  # pragma: no cover
