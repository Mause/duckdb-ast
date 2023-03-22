# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
from os.path import abspath, dirname

project = "duckdb-ast"
copyright = "2023, Elliana May"
author = "Elliana May"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

sys.path.insert(0, abspath(dirname(dirname(__file__))))

extensions: list[str] = ["autoapi.extension", "gh_link"]

templates_path = ["_templates"]
exclude_patterns: list[str] = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

autoapi_dirs = ["../../duckdb_ast"]
autoapi_ignore: list[str] = ["*snapshots*", "*__main__*", "*test_*"]

add_module_names = False
