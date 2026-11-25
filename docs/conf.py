project = "my-arithmetic-nathan"
author = "Nathan Gaillard"

extensions = [
    "sphinx.ext.autodoc",   # lit les docstrings du code
    "sphinx.ext.napoleon",  # comprend le format numpy
]

napoleon_numpy_docstring = True
napoleon_google_docstring = False

html_theme = "sphinx_rtd_theme"
