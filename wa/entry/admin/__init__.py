# -*- coding:utf-8 -*-
from flask import Blueprint

from wa.entry import EntryInterface

admin = Blueprint('admin', __name__,
        static_folder='../static',
#        static_url_path='./static',
        template_folder='../templates')


from flask import render_template, request

from ..forms import LoginForm

@admin.route('/')
def index():
    return '''<html><h1>Hello, WA!</h1></html>'''
#    return render_template('admin/login.html', form=LoginForm(request.form), site=None)

class EntryImpl(EntryInterface):
    def __init__(self, config):
        EntryInterface.__init__(self, config)

    def blueprints(self):
        return [
                (admin, {'url_prefix':'/'}),
                ]
