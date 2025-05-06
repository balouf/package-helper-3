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
{sub-ref}`wordcount-minutes` min read

+++

## 1. Install [UV]

+++

[UV] will handle all the issues related to package management (dependencies, versioning, deployment) for you.

To install it, please follow the instructions from https://docs.astral.sh/uv/getting-started/installation/

:::{admonition} Please install the standalone version
One of the benefit of [UV] is that it does not need to be attached to a specific Python distribution. 
It can use existing distributions if they are compatible with the requirements of a project, or it can ship its own versions. 
This means:
- Having Python installed is not required.
- If you break/update your global Python distribution, [UV] won't be affected.
- You can easily and transparently upgrade your Python version in your UV projects.
:::

Check that it works:

```console
$ uv --version
```

[UV]: https://docs.astral.sh/uv/

+++

## 2. Install Package Helper 3

+++

In a terminal (Anaconda Prompt, Bash, Windows Powershell, etc):

+++

```console
$ uv tool install package-helper-3
```

+++

This will install PH3 as a uv tool. Check that the installation is correct:

```console
$ ph3 --help
```

+++

:::{note} If you have a python distribution with `pip` on your system, you can also install with
```console
$ pip install package-helper-3
```
However, this will tie PH3 to your python distribution.
:::

## 3. Create Accounts on the Websites

+++

Ensure that you have accounts (preferably with the same login) on:

- [GitHub](https://github.com/),
- [PyPI].
- You will need access to [Codecov](https://app.codecov.io/gh/), but you can login with your GitHub account.

:::{note}
In previous PH3 versions, you were asked to get an *API token* from [PyPI]. 
This is not required anymore, as [PyPI] now proposes a [Trusted Publishers](https://docs.pypi.org/trusted-publishers/) approach. 
:::

[PyPI]: https://pypi.org/

+++

## 4. Install Git

+++

*Git will be used to maintain your projects branches locally and remotely.*

Install git: https://git-scm.com/downloads. You may need to restart your computer.

Test it:

```console
$ git --version
```

Ensure your version is recent enough (>=2.40).

+++

## 5. Install Pandoc

+++

PH3 gives you the possibility to insert Jupyter Notebooks in your documentation. 
This requires the installation of the Pandoc converter: https://pandoc.org/installing.html

+++


## 6. Install PyCharm

+++

Install using the binaries available here: https://www.jetbrains.com/pycharm/download/.

+++

### Link PyCharm to your GitHub account

+++

In PyCharm settings: Version Control → GitHub → Add account.

Two options are available:

- Log In with Token. The first time, click on the generate button to open a GitHub page that will create an access token. Copy the token and paste it in PyCharm. PyCharm should remind it but to avoid generating a new token every other week you should keep a copy somewhere else as well (in a very safe place!).  
- Log In via GitHub will open a GitHub page to grant you access (2FA is likely to be required).


:::{admonition} Change the documentation style
We recommend the [Numpy documentation style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html).

In PyCharm settings: Tools → Python Integrated Tools → Docstrings → Docstring format → NumPy.
:::