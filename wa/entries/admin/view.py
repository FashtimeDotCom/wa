# -*- coding:utf-8 -*-

from __future__ import unicode_literals

import os
import json

from flask import Blueprint, redirect, url_for, make_response, render_template
from flask.views import MethodView

from flask.ext.user import current_user, login_required, UserManager, UserMixin, SQLAlchemyAdapter

HERE = os.path.dirname(__file__)

admin = Blueprint('admin', __name__,
        static_folder='./static',
        template_folder='./templates')

@admin.route('/')
def home_page():
    if current_user.is_authenticated():
        return render_template('index.html')
    return redirect(url_for('user.login'))

@admin.route('/menu')
@login_required
def menu():
    m = [
        {
            'name':'配置',
            'href':url_for('admin.config'),
        }
    ]
    return make_response(json.dumps(m))

@admin.route('/config')
@login_required
def config():
    pass