from flask.ext.sqlalchemy import SQLAlchemy
from flask import current_app

db = None

def init_db(app):
    global db
    if not db:
        db = SQLAlchemy(app)
        db.create_all()