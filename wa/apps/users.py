# -*- coding:utf-8 -*-
from bottle import Bottle, request
from paginate_sqlalchemy import SqlalchemyOrmPage

from ..database import plugin
from .. import view
from .. import ui, route
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
    # for i in xrange(100):
    #        t = 'test%d' % i
    #        db.add(Users(t, '111111', t, t+'@example.com', '13800138000'))
    per_page = 10
    page = int(request.query.page or 1)
    items_per_page = int(request.query.items_per_page or 10)

    users = db.query(Users)
    users_page = SqlalchemyOrmPage(users, page=page, items_per_page=items_per_page)
    return ui.main(
        ui.panel_table(
            '用户列表',
            users_page.items,
            Users.head_map,
        ),
        klass='col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2'
    )
