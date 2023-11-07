# Package Helper 3

[![PyPI Status](https://img.shields.io/pypi/v/package-helper-3.svg)](https://pypi.python.org/pypi/package-helper-3)
[![Build Status](https://github.com/balouf/package-helper-3/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/balouf/package-helper-3/actions?query=workflow%3Amain)
[![Documentation Status](https://github.com/balouf/package-helper-3/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/balouf/package-helper-3/actions?query=workflow%3Adocs)
[![License](https://img.shields.io/github/license/balouf/package-helper-3)](https://github.com/balouf/package-helper-3/blob/main/LICENSE)
[![Code Coverage](https://codecov.io/gh/balouf/package-helper-3/branch/main/graphs/badge.svg)](https://codecov.io/gh/balouf/package-helper-3/tree/main)


Package Helper 3 helps to create, develop and maintain a Python package.

It is a fork/mix of https://github.com/audreyr/cookiecutter-pypackage/, https://github.com/francois-durand/package_helper_2/, and https://github.com/fpgmaas/cookiecutter-poetry.

The most prominent feature of Package Helper 3 is a **tutorial** that gives a checklist of how to:

- Create your package in a few minutes with [Cookiecutter][CC] and [Poetry][PO],
- Develop and maintain your package with [PyCharm][PC],
- Host your package on [GitHub][GH] and leverage GitHub actions,
- Publish your package on [PyPi][PP],
- Publicly share your coverage on [Codecov][CO].

A simple **Command-Line Interface** initiates the creation of the package using a **template** of Python package.
Here are the main features of the template:

- Personalize default options.
- Include example files for classes, with examples of documentation and testing.
- Use Poetry for all-in-one management of dependencies and settings.
- Documentation:

  - Use a GitHub action and GitHub Pages to publish the documentation.
  - Use ``sphinx.ext.napoleon`` to benefit from NumPy style of documentation.
  - Use [ReadTheDocs][RTD] or [PyData][PD] themes.
  - Add a "reference" section in the documentation of the package.

- Use a GitHub action to perform unit tests.
- Use a GitHub action to deploy the package on PyPI.
- Generate a local html page displaying the test coverage.
- Use Codecov.

Documentation: https://balouf.github.io/package-helper-3/.

[CC]: https://github.com/audreyr/cookiecutter
[PO]: https://python-poetry.org/
[PC]: https://www.jetbrains.com/pycharm
[GH]: https://github.com
[PP]: https://pypi.python.org/pypi
[CO]: https://app.codecov.io/gh/
[RTD]: https://sphinx-rtd-theme.readthedocs.io/en/stable/
[PD]: https://pydata-sphinx-theme.readthedocs.io/en/stable/