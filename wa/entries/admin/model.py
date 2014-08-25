from flask.ext.user import current_user, login_required, UserManager, UserMixin, SQLAlchemyAdapter
from wa.extensions.database import db

# Define User model. Make sure to add flask.ext.user UserMixin!!
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean(), nullable=False, default=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, default='')

