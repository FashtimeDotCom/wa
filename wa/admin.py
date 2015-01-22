# -*- coding:utf-8 -*-
from collections import OrderedDict
from bottle import Bottle

from .html import *
from .db import Config as ConfigTable
from .db import create_session
from . import ui, view

admin = Bottle()

def get_title():
    db = create_session()
    title = db.query(ConfigTable).filter_by(key='site-title')
    if not title:
        return 'A WA-based site.'
    return title.first().value

def make_nav():
    items = OrderedDict((
        ('首页', admin.get_url('home')),
        ('配置', admin.get_url('config')),
    ))
    return div(
        ul(
            *(li(a(k, href=v)) for k, v in items.iteritems()),
            klass='nav navbar-nav navbar-right'
        ),
        klass='navbar-collapse collapse'
    )

def make_header():
    header = nav(
        ui.container_fluid(
            div(
                a(
                    'Welcome to admin page.',
                    klass='navbar-brand'
                ),
                klass='navbar-header'
            ),
            make_nav(),
        ),
        role='navigation',
        klass="navbar navbar-inverse navbar-fixed-top"
    )
    return header


def make_sidebar(active=None):
    items = OrderedDict((
        ('基本配置', admin.get_url('config')),
        ('用户管理', admin.get_url('config')),
        ('分组管理', admin.get_url('config')),
        ('权限管理', admin.get_url('config')),
        ('应用管理', admin.get_url('config')),
        ('应用商店', admin.get_url('config')),
    ))

    sidebar = ui.sidebar(klass='col-sm-3 col-md-2')
    lis = []
    for k, v in items.iteritems():
        if active == k:
            lis.append(li(a(k, href=v), klass='active'))
        else:
            lis.append(li(a(k, href=v)))
    sidebar(
        ul(
            *lis,
            klass='nav nav-sidebar'
        ),
    )
    return sidebar

def make_head(*a, **kw):
    return head()(
        meta(name="viewport", content="width=device-width, initial-scale=1"),
        script(
            src=r'http://cdn.bootcss.com/bootstrap/3.3.0/js/bootstrap.min.js',
        ),
        link(rel='stylesheet',
             href=r'http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css',
        ),
        link(rel='stylesheet',
             href=r'http://v3.bootcss.com/examples/dashboard/dashboard.css',
        ),
        *a, **kw
    )

@admin.get('/config', name='config')
@view
def config():
    get_title()
    h = make_head(title(get_title()))
    mid = ui.container_fluid(
        ui.row(
            make_sidebar('用户管理'),
            ui.main(
                *([h2('hello, world.')]*30),
                klass='col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2'
            )
        )
    )
    return ui.page(h, body(make_header(), mid))

@admin.get('/', name='home')
@view
def home():
    return h2('hello, world.')


def init():
    return admin
