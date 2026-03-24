import os
import sys

sys.path.insert(0, os.path.abspath(".."))

import {{ cookiecutter.package_name }}

# -- General configuration ---------------------------------------------

# Add extensions here. See https://www.sphinx-doc.org/en/master/usage/extensions/
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.imgconverter",
    "nbsphinx",
    "IPython.sphinxext.ipython_console_highlighting",
    "myst_parser",
    "sphinx_copybutton",
]

# Smart code copy: exclude prompts and output markers
copybutton_exclude = ".linenos, .gp, .go"

# MyST-Parser configuration
myst_enable_extensions = ["linkify", "dollarmath", "colon_fence"]
myst_heading_anchors = 3
myst_links_external_new_tab = True

# Intersphinx: cross-reference other projects' documentation.
# Add or remove mappings depending on which libraries your project uses.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sklearn": ("https://scikit-learn.org/stable", None),
    "ipython": ("https://ipython.readthedocs.io/en/stable/", None),
    "numba": ("https://numba.readthedocs.io/en/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
}

templates_path = ["_templates"]
source_suffix = [".rst", ".md"]
master_doc = "index"

# Project information
project = "{{ cookiecutter.project_name }}"
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.full_name }}"
author = "{{ cookiecutter.full_name }}"

version = {{ cookiecutter.package_name }}.__version__
release = {{ cookiecutter.package_name }}.__version__

language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
            "icon": "fa-brands fa-github",
        },
    ],
    "header_links_before_dropdown": 5,
    "show_nav_level": 2,
    "show_toc_level": 2,
    "navigation_depth": 2,
}

# Uncomment to add custom static files (CSS, JS):
# html_static_path = ["_static"]

# -- Options for HTMLHelp output ---------------------------------------

htmlhelp_basename = "{{ cookiecutter.package_name }}doc"

# -- Options for LaTeX output ------------------------------------------

# Uncomment and adjust for LaTeX/PDF builds:
# latex_elements = {
#     "papersize": "a4paper",
#     "pointsize": "10pt",
# }

latex_documents = [
    (
        master_doc,
        "{{ cookiecutter.package_name }}.tex",
        "{{ cookiecutter.project_name }} Documentation",
        "{{ cookiecutter.full_name }}",
        "manual",
    ),
]

# -- Options for manual page output ------------------------------------

man_pages = [
    (
        master_doc,
        "{{ cookiecutter.package_name }}",
        "{{ cookiecutter.project_name }} Documentation",
        [author],
        1,
    ),
]

# -- Options for Texinfo output ----------------------------------------

texinfo_documents = [
    (
        master_doc,
        "{{ cookiecutter.package_name }}",
        "{{ cookiecutter.project_name }} Documentation",
        author,
        "{{ cookiecutter.package_name }}",
        "One line description of project.",
        "Miscellaneous",
    ),
]
