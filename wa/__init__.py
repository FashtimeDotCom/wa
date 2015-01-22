# -*- coding:utf-8 -*-

# from .plugin import PluginInterface
from .app import App
# from .extensions import init_db
#
# from flask.ext.triangle import Triangle

from functools import wraps

__version__ = (0, 1, 1, 'dev', 0)
__all__ = ('Error',
        'create_app',
        )


def view(f):
    @wraps(f)
    def _(*a, **kw):
        return str(f(*a, **kw))
    return _

class Error(StandardError):
    pass

def create_app(config_file):
    app = App()
    # app.config.from_pyfile(config_file)
    # Triangle(app)
    # init_db(app)
    # app.load_wa_entry()
    return app
