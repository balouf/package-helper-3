# Installation

## Stable release

To install {{ cookiecutter.project_name }}, run this command in your terminal:

```console
$ pip install {{ cookiecutter.project_slug }}
```

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release.

If you don't have [pip] installed, this [Python installation guide] can guide
you through the process.

````{note}
If you want to use {{ cookiecutter.project_name }} as a dependency in a UV-managed project, add it with
```console
$ uv add {{ cookiecutter.project_slug }}
```
````

## From sources

The sources for {{ cookiecutter.project_name }} can be downloaded from the [Github repo].

You can either clone the public repository:

```console
$ git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
```

Or download the [tarball]:

```console
$ curl -OJL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/main
```

Once you have a copy of the source, you can install it from the package directory with:

```console
$ pip install .
```

[github repo]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
[pip]: https://pip.pypa.io
[python installation guide]: http://docs.python-guide.org/en/latest/starting/installation/
[tarball]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/main
