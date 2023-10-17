{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}
        :alt: PyPI Status

.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/build.yml/badge.svg?branch={{ cookiecutter.main_git_branch_name }}
        :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions?query=workflow%3Abuild
        :alt: Build Status

.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/docs.yml/badge.svg?branch={{ cookiecutter.main_git_branch_name }}
        :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions?query=workflow%3Adocs
        :alt: Documentation Status

.. image:: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
        :target: image:: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
        :alt: License
{%- endif %}

.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/{{ cookiecutter.main_git_branch_name }}/graphs/badge.svg
        :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tree/{{ cookiecutter.main_git_branch_name }}
        :alt: Code Coverage

{{ cookiecutter.project_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/.
{% endif %}

--------
Features
--------

* TODO

-------
Credits
-------

This package was created with Cookiecutter_ and the `package-helper-3`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`package-helper-3`: https://balouf.github.io/package-helper-3/
