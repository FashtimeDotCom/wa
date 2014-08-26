# -*- coding:utf-8 -*-

from flask import Blueprint, render_template_string, redirect, url_for
from flask.views import MethodView
from flask.ext.babel import Babel
from flask.ext.mail import Mail

from wa.entry import EntryInterface
from .model import User

admin = Blueprint('admin', __name__,
        static_folder='.../static',
#        static_url_path='./static',
        template_folder='.../templates')


from flask import render_template, request

from wa.forms import LoginForm

from flask.ext.user import current_user, login_required, UserManager, UserMixin, SQLAlchemyAdapter

#class LoginView(MethodView):
#    def get(self):
#        return render_template('admin/login.html', form=LoginForm(request.form), site=None)


#admin.add_url_rule('/users/', view_func=UserAPI.as_view('users'))

#@admin.route('/')
#def index():
#    return '''<html><h1>Hello, WA!</h1></html>'''
#    return render_template('admin/login.html', form=LoginForm(request.form), site=None)



# The '/' page is accessible to anyone
@admin.route('/')
def home_page():
    if current_user.is_authenticated():
        return profile_page()
    return redirect(url_for('user.login'))
    return render_template_string("""
        {% extends "base.html" %}
        {% block content %}
        <h2>{% trans %}Home Page{% endtrans %}</h2>

        {% endblock %}
        """)
    #        <p> <a href="{{ url_for('user.login') }}">{%trans%}Sign in{%endtrans%}</a> or

  #          <a href="{{ url_for('user.register') }}">{%trans%}Register{%endtrans%}</a></p>

# The '/profile' page requires a logged-in user
@admin.route('/profile')
@login_required                                 # Use of @login_required decorator
def profile_page():
    return render_template_string("""
        {% extends "base.html" %}
        {% block content %}
            <h2>{%trans%}Profile Page{%endtrans%}</h2>
            <p> {%trans%}Hello{%endtrans%}
                {{ current_user.username or current_user.email }},</p>
            <p> <a href="{{ url_for('user.change_username') }}">
                {%trans%}Change username{%endtrans%}</a></p>
            <p> <a href="{{ url_for('user.change_password') }}">
                {%trans%}Change password{%endtrans%}</a></p>
            <p> <a href="{{ url_for('user.logout') }}?next={{ url_for('user.login') }}">
                {%trans%}Sign out{%endtrans%}</a></p>
        {% endblock %}
        """)

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
                (admin, {'url_prefix':'/'}),
                ]
