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

# Make a Release

+++

Releases are a key step in the development of a project. A release tells to the world that a new version of your work is available.

You cannot take a release back: if you made a mistake, you will have to make another release to patch your errors. It is therefore important to take your time when you craft a release.

+++

## Bump dependencies in your `pyproject.toml` 

+++

Unless stated otherwise, Poetry uses [carets](https://python-poetry.org/docs/dependency-specification/#caret-requirements) to specify requirements. This basically claims that your package is compatible with new versions of your dependencies as long as these versions do not change too much.

The caret system avoids the burden to constantly update your `pyproject.toml`. However, there is always a moment when your package become incompatible with the latest version of one dependency. Incompatibility can be semantic (e.g. the latest version is outside the caret range) or real (the latest version does not behave like you expect it to do).

Being incompatible with latest versions will not stop anyone from installing your package in a dedicated environment (docker, `venv`, etc) where the version of each dependency is controlled by `poetry.lock`. However, it will be harder and harder for users to use it in their main Python environment. For example, imagine that the `numpy` requirement of your package is `^1.22.4` (e.g. `>=1.22.4` and `<1.23`) and that the latest Pandas requires `numpy>=1.23.2`. This means that everytime you install your package in its latest version you will have to downgrade Pandas, and conversely.

This is why you should regularly bump the versions of our dependencies, and releases are a good opportunity to do that. Forcing users to upgrade to more recent (stable) versions of dependencies is always preferred to forcing downgrades.

+++

If you followed all the steps of the tutorial and installed the Poetry plugin `up`, just enter (inside your project, for example in a PyCharm terminal):

```console
$ poetry up
```

+++

### [optional] Manual upgrade

+++

Optionally, you can look inside `pyproject.toml`. If you see non-caret requirements that you want to bump, you can try to force the update manually with:

```console
$ poetry add package-name@latest
```

Poetry will complain if there are semantic issues, possibly giving you suggestions to address them. 

+++

### Check you didn't break anything

+++

After `pyproject.toml` is updated, refresh `poetry.lock` with:

```console
$ poetry update
```

Run your tests both locally and remotely. If your package is broken:

- Fix it if the error is obvious.
- If not, live to fight another day:
  - Revert your git branch to the last commit before you did `poetry up`. PyCharm has a nice graphical display of git branches that should make it easy.
  - Refresh `poetry.lock` with a `poetry update`.
  - Check that your tests are back on track (locally and remotely).
  - After the current release is done, you should prepare a dedicated release to make your package compatible with latest versions. If possible, preserve backward-compatibility, but not at all cost.

+++

## Make it easy to use

+++

- In the main `__init__.py`, import the classes that you believe users will use on a regular basis. `from my_package import MyClass` is easier to use than `from my_package.subpackage.my_class import MyClass`.
- If you have some notebooks in your documentation (e.g. tutorials), read and run them one last time to check they work and they are relevant.
- Check that the reference section of your documentation is consistent with your actual code, in particular, check that new classes/methods are documented (Sphinx will not complain if they are not).

To reference a class:

```rst
.. autoclass:: my_first_ph3_package.MyClass3
    :members:
```

To reference a module (all the content of a Python file):

```rst
.. automodule:: my_first_ph3_package.cli
    :members:
```

+++

## Bulletproof your tests and documentation

+++

- Be sure that your tests are running OK, both locally in PyCharm and remotely (GitHub actions).
- Check your coverage (locally in `cov/index.html` and/or on [Codecov](https://app.codecov.io/gh/)) and add tests if necessary.
  - It is usually recommended to maintain at least a 70%-80% coverage, but some people see the coverage badge as a motivation to maintain 100%.
  - Coverage is here to give **you** some (relative) confidence that your code will do what you expect, and to ease pinpointing issues when/before they occur. It is not a rating.
  - In particular, don't abuse of `# pragma: no cover` (a magic comment to exclude parts of your code from the coverage statistics) to artificially reach a high coverage.
- Generate the documentation (in PyCharm and/or with GitHub actions) in order to check that it is working.
- If Sphinx issue some warnings, investigate them as it is usually a sign you did something wrong.
- Take some time to browse the resulting documentation as if you were a regular user. Are you happy with it?

+++

## Finalize your release

+++

- Bump the version of your project (unless it is your first release). In PyCharm's terminal:
  - `poetry version patch` (version x.y.z → x.y.(z+1)) when you made a backwards-compatible modification (such as a bug fix).
  - `poetry version minor` (version x.y.z → x.(y+1).0) when you added a functionality.
  - `poetry version major` (version x.y.z → (x+1).0.0) when you changed the API. Note: in versions 0.y.z, the API is not expected to be stable anyway.
- Update the file `HISTORY.rst`:
  - Follow the pattern of previous entries:
    - Title enclosed in dashes lines (`------------`).
    - The two dashes lines should never be shorter than your title.
    - The title should have the version, date of release, and short description.
    - Enter release notes (changes) in short items (lines starting with `*`).
  - Stick to pure `.rst` syntax: never use Sphinx' specific directives such as ``:class:`MyClass` ``.
- Commit/push.
- If you were working on a secondary branch, do what you have to do: pull request to "main" or "master", etc.
- Ensure that you are now in your default git branch ("main" or "master").
- Wait for the last GitHub actions to finish.

+++

## Publish

+++

On [GitHub's website](https://github.com/) go to your project:

- "Releases" → "Create a new release".
- "Choose a tag" → the version you publish prefixed with the letter "v" (e.g. `v0.1.0`) → "Create new tag"
- Add a release title as in `HISTORY.rst`, e.g. `First release`.
- Add release notes as in `HISTORY.rst`, e.g. `* First release on PyPI.`.
- Optionally, check "Set as a pre-release" so the release will be labeled as non-production ready (recommended for early versions of your package).
- Select "Publish release".

After a few minutes, GitHub has finished the built and it is deployed on PyPI. If you want to check:
- Search for your package name on PyPI and check that the version number is correct.
- Check that the readme is correctly rendered on PyPI.
- Note that the PyPI badge may take several more minutes before being updated.
