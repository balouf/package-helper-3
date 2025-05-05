```{highlight} shell
```

# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/balouf/package-helper-3/issues

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement a fix for it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

Package Helper 3 could always use more documentation, whether as part of
the official docs, in docstrings, or even on the web in blog posts, articles,
and such.

### Submit Feedback

The best way to send feedback is to file an issue at
https://github.com/balouf/package-helper-3/issues.

If you are proposing a new feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `package-helper-3` for local
development. Please note this documentation assumes you already have
`UV` and `Git` installed and ready to go.

1. Fork the `package-helper-3` repo on GitHub.

2. Clone your fork locally:
    ```console
    $ cd <directory_in_which_repo_should_be_created>
    $ git clone git@github.com:YOUR_NAME/package-helper-3.git
    ```
   
3. Install your local copy into a virtualenv. Assuming you have uv installed, this is how you set up your fork for local development:

   ```console
   $ cd package-helper-3 
   $ uv sync --all-extras
   ```

4. Create a branch for local development:
    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

    Now you can make your changes locally.

5. Don't forget to add test cases for your added functionality as doctests or in the ``tests`` directory.

6. When you're done making changes, check that your changes pass the tests:
    ```bash
    uv run pytest
    ```

7. Before raising a pull request you should also run `ruff`.:
    ```console
    $ uv run ruff check .
    $ uv run ruff format . 
    ```

8. Commit your changes and push your branch to GitHub:
    ```console
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
    ```

9. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.

2. If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring, and add the feature to
   the list in `README.md`.

3. The pull request should work for the last three stable Python release, e.g. 3.11, 3.12, and 3.13 if Python 3.13 is the latest stable version.
