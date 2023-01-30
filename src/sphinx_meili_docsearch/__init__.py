"""
Front-end search bar for documentation with Meilisearch.

https://github.com/meilisearch/docs-searchbar.js/

"""

from os import makedirs, path
import shutil

import sphinx

version_info = (0, 0, 'dev0')

__version__ = '.'.join(map(str, version_info))

_ROOT_DIR = path.abspath(path.dirname(__file__))


def setup(app):
    app.setup_extension("sphinxcontrib.jquery")
    installed = getattr(app, "_sphinx_meili_docsearch_installed", False)
    if not installed:
        makedirs(path.join(app.outdir, '_static'), exist_ok=True)
        filename = 'docs-searchbar.min.js'
        app.add_js_file(filename, priority=100)
        shutil.copyfile(
            path.join(_ROOT_DIR, filename),
            path.join(app.outdir, '_static', filename)
        )
        app._sphinx_meili_docsearch_installed = True

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
