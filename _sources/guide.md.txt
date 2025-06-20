# Quick Guide

:::{note}
This guide is intended for people that have used PH3 before or with some experience in Python packaging/publishing. 
Otherwise, it is recommended to use the [full tutorial](tutorial.md).
:::

## Preliminaries

- Accounts: [GitHub](https://github.com/), [PyPI](https://pypi.org/).
- Software: 
  - [Git](https://git-scm.com/downloads), 
  - [Pandoc](https://pandoc.org/installing.html), 
  - [UV](https://docs.astral.sh/uv/getting-started/installation/) (standalone preferred), 
  - {ref}`PH3 <install>` (`uv tool install package-helper-3`), 
  - [PyCharm](https://www.jetbrains.com/pycharm/download/).
- PH3: {ref}`create a .cookiecutterrc file <rcfile>` (optional).
- Link PyCharm to your GitHub account.

## Create a new package
- Go to the parent directory of your future project.
- In a terminal:

```bash
$ ph3
$ cd my-project-slug
$ uv sync --all-extras
$ pip install -e . # optional
```

- PyCharm:
  - Check run test & documentation.
  - Check local coverage and built documentation html files.
  - Push project to GitHub.
- Github:
  - Check the gh actions.
  - Check project visibility and `GITHUB_TOKEN` permissions.
  - Setup gh-pages as your public documentation.
  - Install codecov token
  - Tell PyPI to [trust your GitHub action](https://docs.pypi.org/trusted-publishers/).
- Push a small commit, check everything (documentation, badges, coverage) is OK.
- Start working on your project:
  - Frequently run your configurations (tests & documentation).
  - Remind to update docs (especially reference) and tests, in particular when you change the structure.

## Make a release

- Bump your dependencies (`uv remove <pkg> && uv add <pkg> -U`).
- Import important classes in main `__init__.py`.
- Check your docs (references and tutorials).
- Bulletproof tests (coverage!) and documentation building (look up Sphinx warnings).
- Ruff your code (`format` and `check`).
- Bump version of your package (`uv version --bump patch/minor/major`).
- Update `HISTORY.md`, beware of strict Markdown compliance.
- Commit/Push, merge into `main` if you were on a secondary branch.
- Create release on GitHub. Use `vx.y.z` convention for the tag.
- Wait for the badge to be updated, check the release on PyPI.