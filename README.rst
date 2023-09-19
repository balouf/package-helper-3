================
Package Helper 2
================

.. image:: https://github.com/francois-durand/package_helper_2/workflows/docs/badge.svg?branch=master
        :target: https://github.com/francois-durand/package_helper_2/actions?query=workflow%3Adocs
        :alt: Documentation Status

Package Helper 2 explains how to create, develop and maintain a Python package.

The most prominent feature of Package Helper 2 is a **tutorial** that gives a checklist of how to:

* Create your package in a few minutes with Cookiecutter_,
* Develop and maintain your package with PyCharm_.

Optionally, you can also use GitHub_, PyPI_ and Codecov_. For more readability, the
tools that you do not use can be hidden in the tutorial.

Package Helper 2 also provides a **template** of Python package. It is a fork of
https://github.com/audreyr/cookiecutter-pypackage/. Here are the main differences with the original template:

* Personalize default options.
* Include example files for classes, with examples of documentation and testing.
* Documentation:

  * Use a GitHub action and GitHub Pages (instead of ReadTheDocs) to publish the documentation.
  * Use ``sphinx.ext.napoleon`` to benefit from NumPy style of documentation.
  * Use ReadTheDocs theme.
  * Add a "reference" section in the documentation of the package.

* Use a GitHub action (instead of Travis CI) to perform unit tests.
* Use a GitHub action (instead of Travis CI) to deploy the package on PyPI.
* Generate a local html page displaying the test coverage.
* Use Codecov.
* Minor tweaks in ``setup.py``.
* Remove version numbers from ``requirements_dev.txt``.

Documentation: https://package-helper-2.readthedocs.io/.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _PyCharm: https://www.jetbrains.com/pycharm
.. _GitHub: https://github.com
.. _PyPI: https://pypi.python.org/pypi
.. _Codecov: https://app.codecov.io/gh/
