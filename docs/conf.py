import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = "Python module template"
copyright = "2025, ToMansion"
author = "ToMansion"
release = "1.0.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "alabaster"
html_static_path = ["_static"]
