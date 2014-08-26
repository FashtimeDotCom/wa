from flask.ext.sqlalchemy import SQLAlchemy

db = None

def init_db(app):
    global db
    if not db:
        db = SQLAlchemy(app)
        db.create_all()