"""Sphinx configuration."""
project = "DevOps Deployments Metrics"
author = "Flexion, Inc."
copyright = "2023, Flexion, Inc."
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
