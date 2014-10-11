# -*- coding:utf-8 -*-

from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.user import UserManager, SQLAlchemyAdapter

from wa.entry import EntryInterface
from .view import admin
from .model import User

class EntryImpl(EntryInterface):
    def __init__(self, app):
        EntryInterface.__init__(self, app)
        from wa.extensions import db
        db.create_all()
        self.db = db

        self.babel = Babel(self.app)
        self.mail = Mail(self.app)
        self.user_manager = self._init_user()

    def _init_user(self):
        db_adapter = SQLAlchemyAdapter(self.db,  User)       # Select database adapter
        return UserManager(db_adapter, self.app)     # Init Flask-User and bind to app

    def blueprints(self):
        return [
                (admin, {'url_prefix':'/admin'}),
                ]
