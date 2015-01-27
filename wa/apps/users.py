# -*- coding:utf-8 -*-
from bottle import Bottle
from sqlalchemy import Column, String, Integer, Sequence, DateTime

from ..database import Base, plugin
from .. import view
from .. import ui, route
from ..html import *


users = Bottle()

def init():
    users.install(plugin)
    return users

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    username = Column(String(50))
    password = Column(String(50))
    register_time = Column(DateTime(timezone=True))


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


def make_admin_main():
    return ui.main(
        h2('user management.'),
        klass='col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2'
    )
