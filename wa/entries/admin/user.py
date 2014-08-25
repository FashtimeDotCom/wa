from wa.extensions.database import db
from .model import User
from flask.ext.user import current_user, login_required, UserManager, UserMixin, SQLAlchemyAdapter

db_adapter = None
user_manager = None

def init_user(app):
    global db_adapter
    global  user_manager
    if not db_adapter:
        # Setup Flask-User
        db_adapter = SQLAlchemyAdapter(db,  User)       # Select database adapter
        user_manager = UserManager(db_adapter, app)     # Init Flask-User and bind to app