========
Tutorial
========

Package Helper 3 helps you create, develop and maintain a package managed by poetry.
If you use all the tools presented in this tutorial, things will work this way:

* You create the file structure of your package in less than a minute with the `ph3` command.

* You use the IDE PyCharm_. It is configured to:

    * Generate the documentation of your package locally, possibly including Notebooks.
    * Run the unit tests, including the ones from your docstrings (doctests).
    * Generate a local html page displaying what parts of the package are covered by the unit tests.

* Your project is on GitHub_. When you push modifications:

    * GitHub automatically generates the documentation in order to check if it works correctly,
    * If the branch is your default branch ("main" or "master"), Github automatically publishes the documentation online,
    * GitHub automatically runs the unit tests on several versions of Python.
    * Codecov_ displays what parts of the package are covered by the unit tests.

* When you make a *release* on GitHub, GitHub automatically publishes your package on PyPI_. This way, any Python
  user can install it with ``pip install``.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _PyCharm: https://www.jetbrains.com/pycharm
.. _GitHub: https://github.com
.. _PyPI: https://pypi.python.org/pypi
.. _Codecov: https://app.codecov.io/gh/


.. toctree::

   preparation
   creation
   maintain
