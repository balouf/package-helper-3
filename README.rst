================
Package Helper 3
================



.. image:: https://img.shields.io/pypi/v/package-helper-3.svg
        :target: https://pypi.python.org/pypi/package-helper-3
        :alt: PyPI Status

.. image:: https://github.com/balouf/package-helper-3/actions/workflows/main.yml/badge.svg?branch=main
        :target: https://github.com/balouf/package-helper-3/actions?query=workflow%3Amain
        :alt: Build Status

.. image:: https://github.com/balouf/package-helper-3/actions/workflows/docs.yml/badge.svg?branch=main
        :target: https://github.com/balouf/package-helper-3/actions?query=workflow%3Adocs
        :alt: Documentation Status

.. image:: https://img.shields.io/github/license/balouf/package-helper-3
        :target: https://img.shields.io/github/license/balouf/package-helper-3
        :alt: License

.. image:: https://codecov.io/gh/balouf/package-helper-3/branch/main/graphs/badge.svg
        :target: https://codecov.io/gh/balouf/package-helper-3/tree/main
        :alt: Code Coverage

Package Helper 3 helps to create, develop and maintain a Python package.

It is a fork/mix of https://github.com/audreyr/cookiecutter-pypackage/, https://github.com/francois-durand/package_helper_2/, and https://github.com/fpgmaas/cookiecutter-poetry.

The most prominent feature of Package Helper 3 is a **tutorial** that gives a checklist of how to:

* Create your package in a few minutes with Cookiecutter_ and Poetry_,
* Develop and maintain your package with PyCharm_,
* Host your package on GitHub_ and leverage GitHub actions,
* Publish your package on PyPi_,
* Publicly share your coverage on Codecov_.

A simple **Command-Line Interface** initiates the creation of the package using a **template** of Python package.
Here are the main features of the template:

* Personalize default options.
* Include example files for classes, with examples of documentation and testing.
* Use Poetry for all-in-one management of dependencies and settings.
* Documentation:

  * Use a GitHub action and GitHub Pages to publish the documentation.
  * Use ``sphinx.ext.napoleon`` to benefit from NumPy style of documentation.
  * Use ReadTheDocs theme.
  * Add a "reference" section in the documentation of the package.

* Use a GitHub action to perform unit tests.
* Use a GitHub action to deploy the package on PyPI.
* Generate a local html page displaying the test coverage.
* Use Codecov.

Documentation: https://balouf.github.io/package-helper-3/.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _PyCharm: https://www.jetbrains.com/pycharm
.. _GitHub: https://github.com
.. _PyPI: https://pypi.python.org/pypi
.. _Codecov: https://app.codecov.io/gh/
.. _Poetry: https://python-poetry.org/
