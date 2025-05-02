import os
import click


@click.command()
@click.version_option(message="Package Helper 3, version %(version)s")
def main() -> None:  # pragma: no cover
    """
    Package Helper 3 command that creates a UV-powered Python project.

    Cf https://balouf.github.io/package-helper-3/
    """
    cwd = os.path.dirname(__file__)
    package_dir = os.path.abspath(os.path.join(cwd, ".."))
    os.system(f"cookiecutter {package_dir}")
