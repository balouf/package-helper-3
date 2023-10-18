import os
import click


@click.command()
@click.version_option(message="Package Helper 3, version %(version)s")
def main() -> None: # pragma: no cover
    """
    Console script for Package Helper 3.

    Cf https://balouf.github.io/package-helper-3/
    """
    cwd = os.path.dirname(__file__)
    package_dir = os.path.abspath(os.path.join(cwd, ".."))
    os.system(f"cookiecutter {package_dir}")
