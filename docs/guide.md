# Quick Guide

:::{note}
This guide is intended for people that have used PH3 before or with some experience in Python packaging/publishing. 
Otherwise, it is recommended to use the [full tutorial](tutorial.md).
:::

## Preliminaries

- Accounts: [GitHub](https://github.com/), [PyPI](https://pypi.org/).
- PyPi: create a token (and save it!).
- Software: [Python](https://www.python.org/downloads/), [Git](https://git-scm.com/downloads), [Pandoc](https://pandoc.org/installing.html), [Poetry](https://python-poetry.org/docs/#installation), [PH3](https://balouf.github.io/package-helper-3/installation.html) (`pip install package-helper-3`), [PyCharm](https://www.jetbrains.com/pycharm/download/).
- Poetry:

```bash
$ poetry config virtualenvs.in-project true
$ poetry self add poetry-bumpversion
$ poetry self add poetry-plugin-up
```

- Git:

```bash
$ git config --add remote.origin.fetch '^refs/heads/gh-pages'
```

- PH3: [create a .cookiecutterrc file](https://balouf.github.io/package-helper-3/faq.html#Do-I-need-to-enter-my-name/email/github_login-everytime-I-make-a-package?) (optional).
- Link PyCharm to your GitHub account.

## Create a new package
- Go to the parent directory of your future project.
- In a terminal:

```bash
$ ph3
$ cd my-project-slug
$ poetry install
$ pip install -e .
```

- PyCharm:
  - Check run test & documentation.
  - Check local coverage and built documentation html files.
  - Push project to GitHub.
- Github:
  - Check the gh actions.
  - Setup gh-pages as your public documentation.
  - Install codecov and pypi tokens as project secrets.
- Push a small commit, check everything (documentation, badges, coverage) is OK.
- Start working on your project:
  - Frequently run your configurations (tests & documentation).
  - Remind to update docs (especially reference) and tests, in particular when you change the structure.

## Make a release

- Bump your dependencies (`poetry up`).
- Import important classes in main `__init__.py`.
- Check your docs (references and tutorials).
- Bulletproof tests (coverage!) and documentation building (look up Sphinx warnings).
- Bump version of your package (`poetry version patch/minor/major`).
- Update `HISTORY.md`, beware of strict Markdown compliance.
- Commit/Push, merge into `main`/`master` if you were on a secondary branch.
- Create release on GitHub. Use `vx.y.z` convention for the tag.
- Wait for the badge to be updated, check the release on PyPi.