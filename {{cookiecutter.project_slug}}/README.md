{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![PyPI Status](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![Build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions?query=workflow%3Abuild)
[![Documentation Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions?query=workflow%3Adocs)
[![License](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/blob/main/LICENSE)
{%- endif %}
[![Code Coverage](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graphs/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tree/main)

{{ cookiecutter.project_description }}

{% if is_open_source %}
- Free software: {{ cookiecutter.open_source_license }}
- Documentation: https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/.
{% endif %}

## Features

- TODO

## Credits

This package was created with [Cookiecutter][CC] and the [Package Helper 3][PH3] project template.

[CC]: https://github.com/audreyr/cookiecutter
[PH3]: https://balouf.github.io/package-helper-3/
