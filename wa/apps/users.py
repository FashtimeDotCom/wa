# -*- coding:utf-8 -*-
from bottle import Bottle

from ..database import plugin
from .. import view
from .. import ui, route
from ..html import *
from .model import Users

users = Bottle()

def init():
    users.install(plugin)
    return users



@route(users.get, '/signin')
def signin(db):
    pass


@users.get('/signup', name='signup')
@view
def signup(db):
    pass


@users.get('/reset_password', name='reset_password')
@view
def reset_password(db):
    pass


def make_admin_main(db):
    db.add(Users('lai', 'yonghao'))
    return ui.main(
        h2('user management.'),
        klass='col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2'
    )
