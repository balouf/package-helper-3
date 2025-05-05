---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Preliminaries: Once and for All

+++

## Install a Python Distribution if You Don't Have One Already

+++

Ensure that the following requirements are made:

- The Python distribution is recent enough. As a rule of thumb, you should aim to keep one of the last three stable distributions at all times, e.g. 3.10, 3.11, 3.12 if 3.12 is the last stable (non-beta) release.
- The package manager [PIP](https://pip.pypa.io/en/stable/) is included.

+++

## Create Accounts on the Websites

+++

Ensure that you have accounts (preferably with the same login) on:

- [GitHub](https://github.com/),
- [PyPI](https://pypi.org/).

PyPi:

- Go to "Your account" → "Account Settings" → "API tokens" → "Add API token".
- "Token name" → github (for example).
- "Scope" → "Entire account (all projects)".
- Click on "create token". Keep it somewhere safe.

You will need access to [Codecov](https://app.codecov.io/gh/), but you can login with your GitHub account.

+++

## Install Git

+++

*Git will be used to maintain your projects branches locally and remotely.*

Install git: https://git-scm.com/downloads. You may need to restart your computer.

Test it:

```console
$ git --version
```

Ensure your version is recent enough (>=2.40).


Recommended: enter the following command.

```console
$ git config --add remote.origin.fetch '^refs/heads/gh-pages'
```

The command above tells `git` to ignore the branch `gh-pages`. `gh-pages` is the remote branch that hosts your compiled documentation. By default, git will store locally all versions of your documentation, which can take a lot of place for nothing. 

+++

## Install Pandoc

+++

PH3 gives you the possibility to insert Jupyter Notebooks in your documentation. This requires the installation of the Pandoc converter: https://pandoc.org/installing.html

+++

## Install Poetry

+++

[Poetry](https://python-poetry.org/) will handle all the issues related to package management (dependencies, versioning, deployment) for you.

To install it, please follow the instructions from https://python-poetry.org/docs/#installation

Check that it works:

```console
$ poetry --version
```

Additionally the following commands are recommended:

```console
$ poetry config virtualenvs.in-project true
$ poetry self add poetry-bumpversion
$ poetry self add poetry-plugin-up
```

As one can guess, the first command tells that the virtual environment (venv) of a project should be created inside the project instead of within a centralized directory. It facilitates keeping track of the matchings between projects and venvs.

The second command installs a poetry plugin that facilitates the management of the version number of your package.

The last one installs a poetry plugin to automatically update dependencies and bump their versions in the `pyproject.toml` file. 

+++

## Install Package Helper 3

+++

In a terminal (Anaconda Prompt, Bash, Windows Powershell, etc):

+++

```console
$ pip install package-helper-3
```

+++

Check that the installation is correct:

```console
$ ph3 --help
```

+++

## Install PyCharm

+++

Install using the binaries available here: https://www.jetbrains.com/pycharm/download/.

+++

### Link PyCharm to your GitHub account

+++

In PyCharm settings: Version Control → GitHub → Add account.

Two options are available:

- Log In with Token seems to be the recommended way. The first time, click on the generate button to open a GitHub page that will create an access token. Copy the token and paste it in PyCharm. PyCharm should remind it but to avoid generating a new token every other week you should keep a copy somewhere else as well (in a very safe place!).  
- (deprecated) Log In via GitHub will open a GitHub page to grant you access.

+++

### [recommended] Change the documentation style

+++

We recommend the [Numpy documentation style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html).

In PyCharm settings: Tools → Python Integrated Tools → Docstrings → Docstring format → NumPy.
