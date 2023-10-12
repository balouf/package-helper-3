{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}
        :alt: PyPI Status

.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/build/badge.svg?branch={{ cookiecutter.main_git_branch_name }}
        :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions?query=workflow%3Abuild
        :alt: Build Status

.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/docs/badge.svg?branch={{ cookiecutter.main_git_branch_name }}
        :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions?query=workflow%3Adocs
        :alt: Documentation Status
{%- endif %}

{% if cookiecutter.use_codecov == 'y' %}
.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/{{ cookiecutter.main_git_branch_name }}/graphs/badge.svg
        :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tree/{{ cookiecutter.main_git_branch_name }}
        :alt: Code Coverage
{% endif %}


{{ cookiecutter.project_short_description }}

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

This package was created with Cookiecutter_ and the `francois-durand/package_helper_2`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`francois-durand/package_helper_2`: https://github.com/francois-durand/package_helper_2
