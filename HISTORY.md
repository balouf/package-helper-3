# History

## 0.4.0: UV Edition

- UV is now the underlying management tool
- Docs compilation is now MD+Sphinx (using myst-parser)
- PyData is the only theme proposed
- Argparse support removed (click is the only cli package proposed -> if you want something else do the change on your side!)
- Simplified licence choices
- Docker file support removed for now
- Minor improvements

## 0.3.1 (XXXX-XX-XX): Small improvements

- Add git command to exclude gh-pages from fetch

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