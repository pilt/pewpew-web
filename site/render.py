# -*- coding: utf-8 -*-
"""Render content. Typically transform text to HTML. """
import codecs
import os

DEFAULT_EXTENSIONS = {}
ENCODING = 'utf8'

try:
    import markdown
    DEFAULT_EXTENSIONS['.md'] = markdown.markdown
except ImportError:
    pass

class RenderError(Exception):
    pass


class Renderer(object):
    pass


class FileRenderer(Renderer):

    class BadFile(RenderError):
        pass

    class BadExtension(BadFile):
        pass

    class NoFile(BadFile):
        pass

    def __init__(self, app):
        self.app = app
        self._extensions = {}

        for ext, call in DEFAULT_EXTENSIONS.items():
            self.connect(ext, call)

    def connect(self, extension, callable):
        self._extensions[extension] = callable

    def _resolve(self, path):
        if os.path.isabs(path):
            return path
        return os.path.join(self.app.root_path, path)

    def _extension(self, path):
        return os.path.splitext(path)[1]

    def _contents(self, path):
        if not os.path.isfile(path):
            raise self.NoFile("%s isn't a file" % path)
        with codecs.open(path, encoding=ENCODING) as f:
            return f.read()

    def by_extension(self, path):
        ext = self._extension(path)
        call = self._extensions.get(ext)
        if not call:
            raise self.BadExtension("%s isn't a registered extension" % ext)
        return call(self._contents(path))
