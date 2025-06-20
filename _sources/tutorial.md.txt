# Full Tutorial

:::{note} For people who used PH3 before and don't need all explanations, use the [quick guide](guide.md) to remind the key steps.
:::

Package Helper 3 helps you create, develop and maintain a package managed by UV.
If you use all the tools presented in this tutorial, things will work this way:

* You create the file structure of your package in less than a minute with the `ph3` command.
* You use the IDE [PyCharm]. It is configured to:
    * Generate the documentation of your package locally, possibly including notebooks.
    * Run the unit tests, including the ones from your docstrings (doctests).
    * Generate a local html page displaying what parts of the package are covered by the unit tests.
* Your project is on [GitHub]. When you push modifications:
    * GitHub automatically generates the documentation in order to check if it works correctly,
    * If the branch is your default branch ("main"), Github automatically publishes the documentation online,
    * GitHub automatically runs the unit tests on several versions of Python.
    * [Codecov] displays what parts of the package are covered by the unit tests.
* When you make a *release* on GitHub, it automatically publishes your package on [PyPI]. This way, any Python
  user can install it with ``pip install``.


[Cookiecutter]: https://github.com/audreyr/cookiecutter
[PyCharm]: https://www.jetbrains.com/pycharm
[GitHub]: https://github.com
[PyPI]: https://pypi.python.org/pypi
[Codecov]: https://app.codecov.io/gh/


:::{toctree}
preparation
creation
maintain
:::