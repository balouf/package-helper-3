{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![PyPI Status](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![Build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions?query=workflow%3Abuild)
[![Documentation Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions?query=workflow%3Adocs)
[![License: {{ cookiecutter.open_source_license }}](https://img.shields.io/badge/license-{{ cookiecutter.open_source_license }}-yellow.svg)](https://opensource.org/licenses/{{ cookiecutter.open_source_license }})
{%- endif %}
[![Code Coverage](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graphs/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tree/main)

{{ cookiecutter.project_description }}

{% if is_open_source %}
- Free software: {{ cookiecutter.open_source_license }}
- Documentation: <https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/>.
- Github: <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>
{% endif %}

## Features

- TODO

## Quickstart

Install {{ cookiecutter.project_name }}:

```console
$ pip install {{ cookiecutter.project_slug }}
```

Use {{ cookiecutter.project_name }} in a Python project:

```pycon
>>> from {{ cookiecutter.package_name }} import MyClass1
>>> my_object = MyClass1(a=5, b=3)
>>> my_object.addition()
8
```

## Credits

This package was created with [Cookiecutter][CC] and the [Package Helper 3][PH3] project template.

[CC]: <https://github.com/audreyr/cookiecutter>
[PH3]: <https://balouf.github.io/package-helper-3/>
