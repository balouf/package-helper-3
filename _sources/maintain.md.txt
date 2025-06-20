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

(release)=
# Make a Release
{sub-ref}`wordcount-minutes` min read


+++

Releases are a key step in the development of a project. 
A release tells to the world that a new version of your work is available.

You cannot take a release back: if you made a mistake, you will have to make another release to patch your errors. 
It is therefore important to take your time when you craft a release.

+++

## 1. Ruff your code

Pycharm gives you a lot of hints about the quality of your code, but you don't always look at all the signs 
on the right of the screen. You can use [Ruff] to check all your files at once.

```console
$ uv run ruff format .
```

→ Make your code look prettier.

```console
$ uv run ruff check .
```

→ Investigate possible issues (you can use `--fix` to try auto-fixing them if possible).

:::{hint}
Inside the PyCharm terminal the virtual environment should be activated by default so the `uv run` part is not needed:

```console
$ ruff format
$ ruff check --fix
```
:::

[Ruff]: https://docs.astral.sh/ruff/

## 2. Check dependencies in your `pyproject.toml` 

+++

:::{hint}
If you have time, check [the UV documentation about dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/).
:::

Your dependencies (i.e. the packages you rely upon) are handled in two places:

- Inside `pyproject.toml`, you declare (manually or using `uv add`) them, optionally with some version requirements:
  - Use `>=x.y.z` to declare a minimum required version, e.g. `"numpy>=1.23.4"`.
  - Use `<x.y.z` to declare a *stopping point*, e.g. `"numpy>=1.23.4,<2"`.
- The `uv.lock` file describes a combination of specific versions that respects the constraints of `pyproject.toml`:
  - The lock handles all required packages (including dependecies of dependencies of dependencies of depen...) with many metadata, so it can be quite large.
  - See it as a recipe to install *something that works*.
  - **NEVER EDIT IT MANUALLY**. The lock is managed by uv through the `uv sync` command. 

Once in a while, especially when you draft a new release, it can be good to check your versions:
- Upgrade the requirements from your `pyproject.toml` if you need to.
- Use `uv sync --upgrade` to push your version to the limit and test that your code still works.
- If you detect some strong incompatibility, declare a *stopping point* (e.g. `"<2"`).

:::{hint}
To upgrade a package to the latest version in `pyproject.toml` you can do things like
```console
$ uv remove pkg && uv add --upgrade pkg
```
:::

:::{admonition} Prefer future to past

Being incompatible with latest versions will not stop anyone from installing your package in a dedicated environment 
(docker, `.venv`, etc.) where the version of each dependency is controlled by `uv.lock`. 
However, it will be harder and harder for users to use it in their main Python environment.

For example, imagine that your code uses both `numpy` and `pandas`, but your code requires `numpy<2`,
while the latest Pandas requires `numpy>=2`. 
This means that everytime you install your package you will have to downgrade pandas, whereas other packages 
of your distribution may need the latest versions...

To avoid this as much as possible, whenever you need to choose between `pkg1>=x.y.z` and `pkg2<a.b.c` try to enforce 
the first option (sadly, it is not always possible). This will maximize the chances that your package can co-exist 
gracefully with other (well-maintained) packages in a Python distribution.

This also applies to your Python version (the `requires-python` entry of your `pyproject.toml`): if you need to drop 
`python 3.4` compatibility because one of your dependencies did, so be it! 
It is better to be compatible with the last few minor Python versions than with a 10 years old version.
:::

+++

### Check you didn't break anything

+++

After `pyproject.toml` and `uv.lock` are updated, run your tests both locally and remotely. If your package is broken:

- Fix it if the error is obvious.
- If not, live to fight another day:
  - Revert your git branch to the last commit before you updated your `pyproject.toml`. PyCharm has a nice graphical display of git branches that should make it easy.
  - Refresh `uv.lock` with a `uv sync`.
  - Check that your tests are back on track (locally and remotely).
  - After the current release is done, you should prepare a dedicated release to make your package compatible with latest versions. 
  - Reminder: preserve backward-compatibility if possible, but not at all cost.

+++

## 3. Make it easy to use

+++

- In the main `__init__.py`, import the classes that you believe users will use on a regular basis. `from my_package import MyClass` is easier to use than `from my_package.subpackage.my_class import MyClass`.
- If you have some notebooks in your documentation (e.g. tutorials), read and run them one last time to check they work and they are relevant.
- Check that the reference section of your documentation is consistent with your actual code, in particular, check that new classes/methods are documented (Sphinx will not complain if they are not).

To reference a class:

````rst
```{eval-rst}
.. autoclass:: my_first_ph3_package.MyClass3
    :members:
```
````


To reference a module (all the content of a Python file):

````rst
```{eval-rst}
.. automodule:: my_first_ph3_package.cli
    :members:
```
````

These references are to be inserted in a referenced markdown file within the `reference` part of the `docs` directory. 

+++

## 4. Bulletproof your tests and documentation

+++

- Be sure that your tests are running OK, both locally in PyCharm and remotely (GitHub actions).
- Check your coverage (locally in `cov/index.html` and/or on [Codecov](https://app.codecov.io/gh/)) and add tests if necessary.
  - It is usually recommended to maintain at least a 70%-80% coverage, but some people see the coverage badge as a motivation to maintain 100%.
  - Coverage is here to give **you** some (relative) confidence that your code will do what you expect, and to ease pinpointing issues when/before they occur. It is not a rating.
  - In particular, don't abuse of `# pragma: no cover` (a magic comment to exclude parts of your code from the coverage statistics) to artificially reach a high coverage.
- Generate the documentation (in PyCharm and/or with GitHub actions) in order to check that it is working.
- If Sphinx issues some warnings, investigate them as it is usually a sign you did something wrong.
- Take some time to browse the resulting documentation as if you were a regular user. Are you happy with it?

+++

## 5. Finalize your release

+++

- Bump the version of your project (unless it is your first release). In a terminal:
  - `uv version --bump patch` (version x.y.z → x.y.(z+1)) when you made a backwards-compatible modification (such as a bug fix).
  - `uv version --bump minor` (version x.y.z → x.(y+1).0) when you added a functionality.
  - `uv version --bump major` (version x.y.z → (x+1).0.0) when you changed the API. Note: in versions 0.y.z, the API is not expected to be stable anyway.
- Update the file `HISTORY.md`:
  - Follow the pattern of previous entries:
    - Title prefixed with `##`.
    - The title should have the version, date of release, and short description.
    - Enter release notes (changes) in short items (lines starting with `-`).
  - Stick to pure Markdown syntax: never use MystParser specific directives.
- Commit/push.
- If you were working on a secondary branch, do what you have to do: pull request to "main", etc.
- Ensure that you are now in your default git branch ("main").
- Wait for the last GitHub actions to finish.

+++

## 6. Publish

+++

On [GitHub's website](https://github.com/) go to your project:

- "Releases" → "Create a new release".
- "Choose a tag" → the version you publish prefixed with the letter "v" (e.g. `v0.1.0`) → "Create new tag"
- Add a release title as in `HISTORY.md`, e.g. `First release`.
- Add release notes as in `HISTORY.md`, e.g. `- First release on PyPI.`.
- Optionally, check "Set as a pre-release" so the release will be labeled as non-production ready (recommended for early versions of your package).
- Select "Publish release".

After a few minutes, GitHub has finished the built, and it is deployed on PyPI. If you want to check:
- Search for your package name on PyPI and check that the version number is correct.
- Check that the readme is correctly rendered on PyPI.
- Note that the PyPI badge may take several more minutes before being updated.
