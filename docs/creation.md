---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Create Your Package
{sub-ref}`wordcount-minutes` min read


+++

:::{note}
- Creating your package locally should take less than 5 minutes. 
- Full deployment on the different websites  (GitHub, Codecov, Pypi) will take a bit more time, but likely less than 20 minutes.
- Expect a bit more the first time.
- Actual coding time of your package is not included in these estimates.
:::

+++

## 1. Decide What You Want

+++

Before you start, you should decide a few things about your package that PH3 will ask you:

- **Name** / **email** / **github username**. You should know the answer of these questions. If you do not want to re-renter them everytime you make a new project you can write a {ref}`user config file <rcfile>`.
- **Project Name**. This is the name of your project in *human language*. It will be displayed in the documentation. You can (should?) use **title case and spaces** if you have multiple words. For example, *Package Helper 3*.
- **project-slug**. This is where you *store* your package. It will typically be the name of the directory where you develop the package, and the name of your GitHub/PyPi repositories. The convention is to use **lower case and dashes**. Unless you have specific reasons, you should adopt a project slug consistent with your project name. For example, `package-helper-3`.  Also, you should **check that your project slug is not used in [PyPI](https://pypi.org/)**, even if you do not plan to use PyPI for the moment (e.g. to avoid any possible package collision).
- **package_name**. This is the `python` name of your package. It will typically be the name of the subdirectory of your project that contains the actual code. The convention is to use **lower case and underscores**. Unless you have specific reasons, you should adopt a package name consistent with your project name/slug. For example, `import package_helper_3 as ph`.
- **Project description**. One or two sentences that describes the purpose of your project. For example, "*Package Helper 3 helps to create, develop, and maintain a Python package with UV.*"
- **Version**. PH3 adopts the [semantic versioning](https://semver.org/) convention. [As they suggest](https://semver.org/#how-should-i-deal-with-revisions-in-the-0yz-initial-development-phase), we recommend to start your initial development release at 0.1.0.
- **Command line interface (CLI)**. If your package is intended to be always executed from Python, you do not need to care about the CLI. If you intend to execute commands directly from a terminal (Anaconda Prompt, Bash, Windows Powershell, etc), some Python packages are here to help you. PH3 relies on [Click](https://click.palletsprojects.com/en/stable/).
- **Dockerfile**. Do you plan to deploy your package on docker?
- **License**. Which open source license (if any) do you want for your package? Check https://choosealicense.com/ if you need advice.

[RTD]: https://sphinx-rtd-theme.readthedocs.io/en/stable/
[PD]: https://pydata-sphinx-theme.readthedocs.io/en/stable/

+++

## 2. Execute PH3

+++

In a terminal (Anaconda Prompt, Bash, Windows Powershell, etc):

  1. Go to the parent directory of where you want to put the directory of your package, e.g. `D:\GitHub\`, `/home/login/git/`.

  2. Call Package Helper 3:

```console
$ ph3
```

  3. Answer the questions (see above for the meaning). If you leave a question blank, the default proposal (in parenthesis) will be used. Here is an example:

```console
PS C:\Users\loufa\git> ph3
  [1/11] full_name (Fabien Mathieu):
  [2/11] email (fabien.mathieu@normalesup.org):
  [3/11] github_username (balouf):
  [4/11] project_name (Python Boilerplate): My First PH3 Package
  [5/11] project_slug (my-first-ph3-package):
  [6/11] package_name (my_first_ph3_package):
  [7/11] project_description (Python Boilerplate contains all the boilerplate you need to create a Python package.)PH3 packages are quick to make!
  [8/11] version (0.1.0):
  [9/11] Select command_line_interface
    1 - No command-line interface
    2 - Click
    Choose from [1/2] (1): 2
  [10/11] dockerfile [y/n] (n):
  [11/11] Select open_source_license
    1 - MIT
    2 - GPL-3.0-or-later
    3 - BSD-3-Clause
    4 - ISC
    5 - Apache-2.0
    6 - Not open source
    Choose from [1/2/3/4/5/6] (1):
```

:::{note}
In your file manager, open the directory of your package: the whole file structure is now in there!
:::

+++

## 3. Install Your Project

+++

Developing a project and using a package are two different things. Each usage has its own rules!

+++

### Install a development environment

+++

In a terminal prompt, go to the project directory (we will use `my-first-ph3-package` as a running example) and enter:

```console
$ uv sync --all-extras
```

Wait for the installation to complete and you're done!

+++

:::{tip}

The command `uv sync` creates a virtual environment for developing your package, located in your project directory in a `.venv` subdirectory.

The package is installed in *editable* mode. That means that everytime you load the package with `uv`, 
the current version of your code will be used, not the one from the installation time.
:::

:::{note}
Before `uv`, virtual environments were usually *activated* (`.\.venv\Scripts\activate`).

With `uv`, you still can activate but don't need to. The usual practice is to execute `uv run ...`. This will activate on-the-fly the environment and exit after use.

For example, after having created your venv, you can test that your environment is well configured by launching python:

```console
$ uv run python
Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

This will start a Python session where your package is available.

```python
>>> from my_first_ph3_package import MyClass1
>>> res = MyClass1(2, 3)
>>> res.my_string
'a = 2 and b = 3'
```

If you choose a CLI, you can also try and run the default script:

```console
$ uv run my_first_ph3_package --help
Usage: my_first_ph3_package [OPTIONS]

  Console script for my-first-ph3-package.

Options:
  --help  Show this message and exit.
```

:::

+++

### Install on your default Python distribution

+++

At this point, your Python package is only available in its dedicated development virtual environment. 

If you have a Python distribution ({ref}`this is not required <pythonless>`) and want to use it more broadly 
(e.g. if you want to run Jupyter Notebooks, combine it with other packages, etc...):
+++

- Use a terminal prompt **outside** your dedicated environment (check that the package name is not present in the prompt);
- Go to the project directory and install your package:

```console
$ pip install -e .
```

+++

The `-e` option means that you will install the package in *editable* mode, like for the dedicated environment.

The `.` (dot) tells that the package to install is in the working directory.

+++

Your package is now available outside your dedicated environment! For example, if you chose a CLI:

```console
$ my_first_ph3_package
Replace this message by putting your code into my_first_ph3_package.cli.main
See click documentation at https://click.palletsprojects.com/
```

+++

You can also try to open the Notebook `my-first-ph3-package/docs/tutorials/tutorial.ipynb` and check that the calls to the package are working fine.

+++

## 4. Open your Project with PyCharm

+++

To open your project:

- Inside PyCharm, you can choose "Open" and select the directory of your project (`project-slug`).
- Alternatively, if you installed PyCharm with context menu, you can right-click the directory in your favorite file manager and select "Open folder as PyCharm project"


In the bottom right part of the window, you will probably see some background tasks running. 
Wait until they are finished. 
In particular, wait until PyCharm discovered your dedicated environment, 
e.g. when `<No interpreter>` is replaced by something like `Python 3.12 (my-first-ph3-package)` 
(it is usually displayed in the lower right corner).

:::{note}
Some users reported that PyCharm sometimes fails to locate the dedicated environment. If that happens, try to open (in PyCharm) the main Python file of the project, PyCharm should then propose to use the environment in a banner.
:::

+++

### Run your tests locally

- In PyCharm: menu Run → Run → All Tests. It runs all the tests of the project. PH3 provides in its template examples that you can re-use if you are new to testing (e.g. in `my_class_1.py`).

- Open the file `cov/index.html` (in your web browser). It displays what parts of your code are covered by the tests.

### Build your documentation locally


- In PyCharm: menu Run → Run → Generate docs. It generates the html documentation of your project. The template provides examples of classes, such as the file my_class_1.py. You can use them as models if you are new to Sphinx documentation.

- Open the file `build/index.html` (in your web browser). It displays the html documentation of your project.

+++

## 5. Go GitHub

+++

First thing to do is create the GitHub repo of your project. In PyCharm:

- From the file `pyproject.toml` of your package, copy the `description` value, e.g. "PH3 packages are quick to make!" in the example above. You will paste it in the form below.
- Menu Version Control → Share project on GitHub.
- Fill in the form and validate, e.g.:
```console
New repository name: my_first_ph3_package
Remote name: origin
Description: PH3 packages are quick to make!
```

- Accept to add all the files as proposed by PyCharm.

In a browser, you can go to your GitHub account to check that everything is there.

:::{admonition} Check repo visibility
GitHub repos can be private or public. 
Some features like publishing your documentation on GitHub pages are only available on public repos unless you have a paid account. If you set up your repo to private, you can switch visibility to public on the settings menu (the *Danger Zone* down the screen).
:::
+++

:::{admonition} Check Workflow permissions
GitHub actions can use a `GITHUB_TOKEN` to perform different operations on the repo. 
PH3 need thetoken to have `read` **AND** `write` permission, e.g. to publish the documentation on a dedicated branch.
To avoid errors, go to Settings → Actions → General → Workflow permissions and check that `GITHUB_TOKEN` is `read and write`.
:::

### Check GitHub actions

+++

In GitHub:

- GitHub page of your package → Actions.
- Check that the actions are successes (it may take several minutes). 
  - The "build" action runs the tests of the package. Default PH3 triggers are:
    - When something is pushed on the default branch ("main").
    - When there is a pull request.
    - At 5:30 am the 1st and 15th of each month.
  - The "docs" actions builds the documentation when something is pushed. It publishes it online if the branch is your default git branch ("main").
  - The "release" action should not have been triggered at this point. It will run when you release a version to publish it on PyPi.

:::{note}
If the permissions of `GITHUB_TOKEN` were initially too restrictive, the initial build of `docs` may have failed. 
After permissions have been fixed, the action should work as expected.
:::
+++

### Declare your documentation

+++

Tell GitHub Pages that the documentation files are in the "gh-pages" branch of your project:

- Settings → Pages → Build and deployment
- Check that Source is "deploy from a branch".
- Branch → "gh-pages", "/ (root)".
- Save.

+++

### Link with Codecov

+++

Configure Codecov so you can publicly expose the test coverage of your package:

- On [Codecov's website](https://app.codecov.io/gh/), log in with your GitHub account. On your main page, locate your project and click the corresponding `Setup repo >` link.
- You may have to wait for syncing before it appears. If it takes too long try the `Can't find your repo? Try re-sync` link (but you may have to wait anyway).
- In your project, copy the Codecov token.
- Back to GitHub: Settings → Secrets and variables → Actions → New repository secret. Name: `CODECOV_TOKEN`. Value: paste the codecov token. 

+++

### Link with [PyPI]

[PyPI] has a [Trusted Publisher policy](https://docs.pypi.org/trusted-publishers/) to allow GitHub to publish new versions on your behalf.

Follow the quickstart instructions there to enable publishing. You should enter these information in the `GitHub` tab:

- PyPI Project Name: your project slug (e.g. `my-first-ph3-package`)
- Owner: Your GitHub username
- Repository name: your project slug (e.g. `my-first-ph3-package`)
- Workflow name: `release.yml`
- Environment name: `pypi`

[PyPI]: https://pypi.org

+++

### Test on a first commit

+++

In PyCharm, make a slight modification, e.g. in the file `README.rst`. Then commit/push:

- From the VC menu, choose Commit (or `Ctrl+k`).
- Enter a commit message, click on `Commit`.
- From the VC menu, choose Push (or `Ctrl+Shift+K`).
- Click on Push.

Then check that everything is working online:

- GitHub page of your package → Actions. Wait until your actions are finished.
- Check the documentation:
  - GitHub page of your package (main page) → near the bottom of the page, follow the link to your documentation. Check that the documentation is there.
  - In the table of contents, click on the first page (e.g. My Toy Package). Depending on your initial choice of options, you should have up to five badges:
    - PyPI: package or version not found (there will be the version number after your first release).
    - Build: passing.
    - Docs: passing.
    - License: the license you choose.
    - Codecov: with a percentage.
  - In the table of contents: Reference → MyClass1. You should see the documentation of the first example of class provided by the template.

- Check your test coverage:
  - GitHub page of your package (main page) → near the bottom of the page, click on the Codecov badge.
  - You can navigate in your project to see what parts of the code are covered by the tests.

If you wish, you are now ready to release your first version! (cf {ref}`release`). But maybe you should add some real code first.

+++

## 6. Time to Code!

- Replace the toy code provided by PH3 with your actual code.
- {ref}`Add/remove dependencies <dependencies>` according to your needs.
- Right click on PyCharm's project tree to create new *modules* (i.e. Python files) and *(sub)packages* (directories with a `__init__.py` file).
- If you manually copy files in your project, don't forget to add them to Git.
- Keep in mind that your project is not just your source code
  - Update your documentation:
    - Check that your `reference` section is consistent with your actual package.
    - Update your documentation notebooks if you have some.
    - Check the sphinx warnings when you build the documentation.
  - Update your tests:
    - Update your docstrings.
    - Update your `tests` directory.
    - Check your coverage.

:::{hint}
Your documentation uses [MyST], a flavor of Markdown that allows many nice things (boxes, maths, footnotes...). 
Don't hesitate to [browse its documentation][MyST] to see the possibilities!
:::

[MyST]: https://myst-parser.readthedocs.io/en/v0.15.1/index.html
