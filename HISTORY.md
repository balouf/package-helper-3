# History

## 0.6.1 (2026-03-27): Software Heritage integration

* Add Software Heritage archival documentation and guidance (creation, guide, FAQ, preparation)
* Add Software Heritage badge to README

## 0.6.0 (2026-03-24)

### Breaking Changes
* Drop Python 3.10 support (`requires-python` bumped to `>=3.11`)

### Updates
* Migrate docs deployment from `gh-pages` branch to GitHub Actions artifact upload (both host and template)
* Add VS Code support in documentation: preparation, creation, and tutorial pages now cover both PyCharm and VS Code
* Add new "LLM-Assisted Package Maintenance" documentation page
* Add `[tool.ruff] target-version` configuration to both host and template `pyproject.toml`
* Update UV version in all workflows: 0.9.28 → 0.11.0
* Update copyright year in docs to 2023-2026
* Clean up `docs/conf.py` boilerplate comments (both host and template)
* Remove stale `[tool.setuptools]` section from `pyproject.toml`
* Add `.vscode/` to host `.gitignore`

### Template improvements
* Add VS Code configuration files (`.vscode/settings.json`, `.vscode/tasks.json`)
* Merge `.coveragerc` into `pyproject.toml` (single source of truth)
* Remove `sphinx.ext.githubpages` extension (no longer needed with artifact deployment)
* Update Dockerfile: Python 3.12 → 3.13, UV 0.6.16 → 0.11.0
* Fix rst double-colon artifacts in `CONTRIBUTING.md`
* Remove unused `import sys` from template `cli.py`
* Remove stale `[LICENSE]` section from `.editorconfig`
* Remove stray `.pyc` file from template

### Dependency bumps
* Bump dev dependency minimums: `ipython` >=8.35.0 → >=9.0.0, `myst-parser` >=4.0.1 → >=5.0.0, `pytest-cov` >=6.1.1 → >=7.0.0

### Fixes
* Update docs to reflect GitHub Pages "GitHub Actions" source (instead of `gh-pages` branch)
* Update `GITHUB_TOKEN` permission guidance in docs (no longer needs write for docs deployment)

## 0.5.0 (2026-02-02): Dependency Modernization

### Breaking Changes
* Replace Black formatter with ruff-format in pre-commit hooks

### Updates
* Add Python 3.13 and 3.14 support to CI test matrix
* Update pre-commit hooks:
  - pre-commit-hooks: v4.4.0 -> v6.0.0
  - ruff-pre-commit: v0.0.230 -> v0.14.14 (migrated to astral-sh)
  - Remove Black (replaced by ruff-format)
* Update UV version in all workflows: 0.7.2 -> 0.9.28
* Update ruff dependency: >=0.11.8 -> >=0.14.0
* Template now generates projects with updated configurations

### Fixes
* Fix typo "dependecies" in docs/maintain.md
* Fix typo "poetry.toml" in docs/faq.md
* Update outdated Poetry references to UV in FAQ

## 0.4.5 (2025-06-20): Minor update

* Fix Jekyll invading actions by default.
* Fix deploying condition for the `docs` GH action.
* Fix bad `note` environment in `installation.md`


## 0.4.3 (2025-05-07): Minor update

* Documentation fully re-written to follow the new workflow.
* Fix a few bugs (e.g. misconfiguration of some *GitHub Actions*).


## 0.4.2 (2025-05-05): UV Edition

This version aims at making things simpler and faster, mostly thanks to [UV].

- [UV] is now the underlying management tool
- Docs compilation is now 100% Markdown (using [Sphinx]+[MyST])
- [PyData] is the theme proposed
- [click] is the cli interface
- License is now defined in the `pyproject.toml` (no more dedicated `LICENCE` file)
- Add possibility to install PH3 as a UV tool so you don't need any Python distribution installed.
- Minor improvements (e.g. update versions and such)

[UV]: https://docs.astral.sh/uv/
[Sphinx]: https://www.sphinx-doc.org/en/master/
[MyST]: https://myst-parser.readthedocs.io/en/v0.15.1/index.html
[PyData]: https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html
[click]: https://click.palletsprojects.com/en/stable/

## 0.3.0 (2023-11-07): Incorporate feedbacks

- Add option to choose PyData theme (new default).
- PH3 documentation now uses PyData.
- Remove choice of default git branch. It is now always `main`.
- Add markdown support:
  - Root documentation files (e.g. `README.md`) are in Markdown format for simplicity;
  - Structural documentation files (inside `docs/`) are in reStructuredText format for flexibility;
  - Boilerplate tutorials stay in notebook format (`.ipynb`).
- Lots of typos squashed.
- Dependencies bumped.

## 0.2.0 (2023-10-20): Fully working release

- CLI command (ph3) has been tested in real conditions.
- Tutorials to describe the main steps (installation, creation, release).
- One recap tutorial to remind the important stuff at one glance.
- FAQ for specific/advanced/optional questions.
- Many bugs squashed.


## 0.1.1 (2023-10-17): Bugfix

- Actual template was not included in the wheel.

## 0.1.0 (2023-10-17): First release

- Cookiecutter generates automatically the run configurations for PyCharm: "All tests" and "Generate docs".
- It is possible to choose "main" or "master" as the default git branch; default to "main".
- Generate a local html page displaying the test coverage.
- Missing features: publish on pypi template action and tutorial
