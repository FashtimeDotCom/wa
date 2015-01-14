# -*- coding:utf-8 -*-

# from .plugin import PluginInterface
from .app import App
# from .extensions import init_db
#
# from flask.ext.triangle import Triangle

__version__ = (0, 1, 1, 'dev', 0)
__all__ = ('Error',
        'create_app',
        )

class Error(StandardError):
    pass

def create_app(config_file):
    app = App()
    # app.config.from_pyfile(config_file)
    # Triangle(app)
    # init_db(app)
    # app.load_wa_entry()
    return app
