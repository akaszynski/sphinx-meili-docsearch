# Configuration file for the Sphinx documentation.
import os

# -- Project information -----------------------------------------------------
project = "sphinx-meili-docsearch"
copyright = "2023, Alex Kaszynski"
author = "Alex Kaszynski"

# The full version, including alpha/beta/rc tags
release = "0.0.dev0"

# -- PyVista Configuration for the Gallery-------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_meili_docsearch",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "logo": {
        "image_light": "logo-light.png",
        "image_dark": "logo-dark.png",
    }
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

