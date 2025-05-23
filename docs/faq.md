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

# F.A.Q.

+++
(dependencies)=
## How to manage dependencies (third-party packages)?

+++

The most useful command you need to know is

```console
$ uv add <pkg-name>
```

But UV offers a lot more. Don't hesitate to browse its [documentation](https://docs.astral.sh/uv/concepts/projects/dependencies/).

+++

## I have a great package based on `setup.py`. How can I switch to `uv`?

+++

I personally find that making a manual conversion has a good simplicity/efficiency trade-off.

- Start with a fresh `git clone my_package` (no venv or anything).
- Open `setup.py` or other files in some text editor to have a look at your parameters (current version, description, requirements...)
- Create your `pyproject.toml` inside your project directory with

```console
$ uv init
```

- Add dependencies with `uv add` (use `--dev` to isolate dev dependencies like `sphinx`).
- By default, poetry associates `readme` with `README.md`. If your readme is in another format, e.g. `README.rst`, convert it to Markdown ([rst2myst is great](https://rst-to-myst.readthedocs.io/en/latest/index.html)).


Depending on your dependencies, `UV` may complain of compatibility issues.

- Resolve them by editing `pyproject.toml` and running `uv sync` until it works.
- UV usually gives useful suggestions when it fails.
- Rule of thumb: don't hesitate to sacrifice compatibility with older Python versions. For example, if your current version has Python >= 3.6 compatibility and the numpy (the latest version, which UV suggested you to install) requires Python>=3.9, just accept that your future releases will have Python>=3.9 compatibility.

Open your project in PyCharm and run your tests. Adjust until they work.

Most `.ini` files, e.g. for tox or pytest, can be transferred into `pyproject.toml`. Google how to do it or adapt a previous PH3 project.

You should now be able to remove the legacy files. Check you didn't break anything.

Push your changes on GitHub (preferably on a secondary branch) to check it works.

Bump&Release!

## I have a great package based on `poetry`. How can I switch to `uv`?

In theory, you just have two things to do:

- Upgrade the `pyproject.toml` to the UV format. This can be tedious, don't hesitate to Google it or copy from a PH3 dummy package.
- Install with `uv sync`.
- Remove the old `poetry.lock` and add to git the new `uv.lock`.

+++

(rcfile)=
## Do I need to enter my name/email/github_login everytime I make a package?

+++

No.

If you use Package Helper 3 / Cookiecutter a lot, you’ll find it useful to have a user config file. By default Cookiecutter tries to retrieve settings from a `.cookiecutterrc` file in your home directory (e.g. `c:\Users\login` on Windows). Recommended template for PH3:

```yaml
default_context:
    full_name: "Your Name Here"
    email: "my.name@example.com"
    github_username: "my-gh-username"
```

(From https://cookiecutter.readthedocs.io/en/stable/advanced/user_config.html)

+++

## How to call a method from a prompt?

+++

With `pyproject.toml`, you can easily setup commands to be executed directly from a prompt (a.k.a. Command Line Interface, CLI). This is made by linking some keywords (*entry points*) to methods of your package. The declarations are made in the `[project.scripts]` section of `pyproject.toml`. 

For example, if you choose a CLI when creating your project, you should have something like this:

```toml
[project.scripts]
my_first_ph3_package = 'my_first_ph3_package.cli:main'
```

The key is the *entry point*, e.g. the command that will trigger the execution of your script. By default, PH3 sets up an entry point name like the package name but you may change that!

The value tells where is located the method you want to execute. In the example above, it is the `main` method of the `cli.py` file located at the root of the `my_first_ph3_package` package.

**Entry points and editable mode**: it is important to understand that the *editable* mode of a package is *passive*. It just tell Python to look directly at the location of the package you are working on instead of the place where regular packages are installed. In particular, just editing the `pyproject.toml` has no effect on the available entry points so if you change them you need to refresh your installations:

```console
$ uv sync
$ pip install -e . -U
```

(the last one is optional, in case you have a Python distribution installed)

+++

## How to add a logo?

It's always nice to brand your package with a logo and/or a favicon.

- Create your pictures. If you have no inspiration, you can use https://favicon.io/favicon-generator/ to make one in a few seconds from a text (e.g. the acronym of your package). 
- Edit your documentation files to include them.

favicon is just a regular `png` file with small dimensions (16X16 or 32X32) and extension `.ico`. To include it, edit your `docs/conf.py` file to include:

```python
html_favicon = 'filename_of_the_fav.ico'
```

Same thing for the logo, which will be displayed in the upper left corner of your documentation:

```python
html_logo = 'filename_of_the_logo.png'
```

By default, Sphinx will look for the files in the directory where `conf.py` lies (usually `docs`). If you like to clean up, you can create a dedicated subdir for static files, like `_static`, and tell `conf.py` about it:
```python
html_static_path = ['_static']
```

+++

## How to do *some exotic stuff* with UV?

+++

Google is your friend. Most of the time, you just need a special line in `pyproject.toml`.

The [UV documentation](https://docs.astral.sh/uv/concepts/projects/) contains many useful examples.


:::{admonition} Example: Install spacy language model

Spacy usually requires a language model which you need to install separately, e.g. with `python -m spacy download en_core_web_sm`. 
It seems that you can do this inside `poetry.toml`:

```toml
[tool.uv.sources]
en_core_web_sm = { url = "https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0.tar.gz" }
```
This avoids you to have to run a post-install script, but you will have to manually maintain consistency between the versions of spacy and your model.
:::


+++

## Which Python distribution should I use?

(pythonless)=
:::{important}
You don't need any Python distribution if you use UV!
:::

However, it can be comfortable to be able to run `python` from any shell, and you need a proper Python installation for that.

There is no good answer here as long as you don't install a 2.7 version. It's like asking Mac or PC.

But if you have no idea, here are two popular distributions:

- [Anaconda](https://www.anaconda.com/download)
  - Pros: Anaconda installs by default a lot of common packages so you will not have to install them yourself (e.g. Numpy, Matplotlib, Jupyter, Pandas...).
  - Cons: the distribution is very large to install and the included package manager (conda) can clash with PIP, provoking dependency conflicts.
- [Vanilla Python](https://www.python.org/downloads/)
  - Pro: Minimalist → as clean as possible.
  - Cons: Minimalist → you'll have to install your favorite packages on your own.
  
Anaconda is recommended for beginners who do not want to get too dirty in package management and are not afraid of re-installing the distribution once a year because of clash in package management.

Vanilla Python is recommended for more experienced users who wants a full control of their environment(s) and are not afraid of re-installing the distribution once a year to stay sharp and up-to-date.

+++

## What's the git default branch name?

+++

The git default branch name is used to name the principal branch in your git projects. It used to be "master" but the current standard is to call it "main". When installing `git` you should setup "main" as default during the setup. The important thing is that the settings of your git application should be consistent with the setting of your **new** projects (once properly initiated, a project has its own branch system so there is no issue to manage an existing "master"-flavored project with a "main"-flavored git). 

To change the default branch name after installation you can try:

```console
$ git config --global init.defaultBranch main
```

+++

## I am used to `setup.py` to deploy my package. Why should I bother with Poetry?

+++

Before the `pyproject.toml` approach, managing packages required multiple files, e.g.:

- A `setup.py` file with some informations about the package and its dependencies;
- A `requirements.txt` file to facilitate the installation of dependencies with `pip`;
- A `requirements_dev.txt` file to describe the additional packages required to develop the package;
- Some dedicated config files like `tox.ini`, `pytest.ini`, ...

All these files were to be update manually in most cases, leading to mismatch/conflicts between dependencies. And the environments were to be handled separately.

With UV, all is concentrated in two files:

- `pyproject.toml` tells everything you need to know about your package, nicely split into sections.
- `uv.lock` gives an exhaustive set of exact versions (including where to find them) that works.

The benefits are:

- `pyproject.toml` can be automatically maintained by uv commands to add/remove dependencies, update versions, ...
- If required, it is easy to perform manual editions.
- You never need to edit `uv.lock`, it is automatically managed.
- Dependencies can be split into groups, e.g. optional dependencies (e.g. graphic packages), dev dependencies... and you can customize the groups you want to install.
- Dependencies not available on `pip` can be integrated (e.g. private repositories).
- Installing your development environment is simple as `$ uv sync`. Installing the package in the main environment or pushing to pypi are also straightforward.

I used [Package Helper 2 (PH2)](https://package-helper-2.readthedocs.io/en/latest/index.html) a lot to create my own packages. It was a great tool to bootstrap a new package in a couple of minutes, but it was based on a `setup.py` approach. After one bite of Poetry[^1], I realized `setup.py` was not an option for me anymore. This motivated the creation of [Package Helper 3](https://balouf.github.io/package-helper-3/index.html).

[^1]: Poetry is the precursor of UV. Notably, it introduced `pyproject.toml`.
+++

## Why isn't feature *XXX* available in PH3?

+++

PH3 is a relatively simple BoilerPlate for Python packages. It lacks many features.

- If you think *XXX* is a must for PH3, you can [Make a PR](https://balouf.github.io/package-helper-3/contributing.html) that implements *XXX*.
- Many other BoilerPlates are available on the Web. For example, https://github.com/BrianPugh/python-template offers much more possibilities than PH3.

## GitHub Actions Issues

### `The process '/usr/bin/git' failed with exit code 128`

Check Workflow Permissions:
- Go to your repository's Settings > Actions > General > Workflow permissions.
- Ensure that "Read and write permissions" is enabled for the GITHUB_TOKEN