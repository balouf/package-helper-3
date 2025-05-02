#!/usr/bin/env python
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()

if __name__ == '__main__':

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        (PROJECT_DIRECTORY / '{{ cookiecutter.package_name }}' / 'cli.py').unlink()

    if not {{ cookiecutter.dockerfile }}:
        (PROJECT_DIRECTORY / 'Dockerfile').unlink()
