# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.abspath("../../../parser"))
sys.path.append(os.path.abspath("../../.."))
sys.path.append(os.path.abspath("../.."))
sys.path.append(os.path.abspath(".."))

html_theme = "press"

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}


# The master toctree document (without the file extension)
master_doc = "index"

project = "strlib"
copyright = "2023, Joshua Rose"
author = "Joshua Rose"
release = "0.0.0-development"

html_static_path = ["_static"]

extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "myst_parser",
    "sphinx.ext.todo",
]

# paths that contain templates, *relative* to this file.
templates_path = ["_templates"]
