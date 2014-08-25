# -*- coding:utf-8 -*-

from .plugin import PluginInterface
from .app import App
from .extensions.database import init_db
from flask.ext.babel import Babel

__version__ = (0, 1, 1, 'dev', 0)
__all__ = ('PluginInterface',
        'create_app',
        )

babel = None

class Error(StandardError):
    pass

def create_app(config_file):
    app = App(__name__)
    app.config.from_pyfile(config_file)
    global babel
    babel = Babel(app)                              # Initialize Flask-Babel
    init_db(app)
    app.load_wa_entry()
    from .entries.admin.user import init_user
    init_user(app)
    return app

