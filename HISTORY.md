# History

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
