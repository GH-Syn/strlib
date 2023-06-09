# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.abspath("../../.."))
sys.path.append(os.path.abspath("../.."))
sys.path.append(os.path.abspath(".."))

html_theme = "press"

project = 'strlib'
copyright = '2023, Joshua Rose'
author = 'Joshua Rose'
release = '0.0.0-development'

html_static_path = ['_static']

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
