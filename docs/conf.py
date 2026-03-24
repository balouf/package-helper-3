import os
import sys

sys.path.insert(0, os.path.abspath(".."))

import package_helper_3

# -- General configuration ---------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "IPython.sphinxext.ipython_console_highlighting",
    "sphinx.ext.intersphinx",
    "sphinx.ext.imgconverter",
    "myst_parser",
    "sphinx_copybutton",
]

copybutton_exclude = ".linenos, .gp, .go"

myst_enable_extensions = ["linkify", "dollarmath", "colon_fence"]
myst_heading_anchors = 3
myst_links_external_new_tab = True

templates_path = ["_templates"]
source_suffix = [".rst", ".md"]
master_doc = "index"

project = "Package Helper 3"
copyright = "2023-2026, Fabien Mathieu"
author = "Fabien Mathieu"

version = package_helper_3.__version__
release = package_helper_3.__version__

language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------

html_theme = "pydata_sphinx_theme"
html_favicon = "favicon.ico"
html_title = f"Package Helper 3 v{package_helper_3.__version__}"
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/balouf/package-helper-3",
            "icon": "fa-brands fa-github",
        },
    ],
    "header_links_before_dropdown": 5,
    "show_nav_level": 2,
    "show_toc_level": 2,
    "navigation_depth": 2,
}

# -- Options for HTMLHelp output ---------------------------------------

htmlhelp_basename = "package_helper_3doc"

# -- Options for LaTeX output ------------------------------------------

latex_documents = [
    (
        master_doc,
        "package_helper_3.tex",
        "package_helper_3 Documentation",
        "Package Helper 3",
        "manual",
    ),
]

# -- Options for manual page output ------------------------------------

man_pages = [
    (master_doc, "package_helper_3", "package-helper-3 Documentation", [author], 1)
]

# -- Options for Texinfo output ----------------------------------------

texinfo_documents = [
    (
        master_doc,
        "package_helper_3",
        "package_helper_3 Documentation",
        author,
        "package_helper_3",
        "One line description of project.",
        "Miscellaneous",
    ),
]
