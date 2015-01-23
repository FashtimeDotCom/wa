# -*- coding:utf-8 -*-
from collections import OrderedDict

from bottle import Bottle, redirect, request

from .html import *
from .database import Config as ConfigTable
from .database import create_session, plugin
from . import ui, view, users


admin = Bottle()

def get_title():
    db = create_session()
    title_conf = db.query(ConfigTable).filter_by(key='site_title').first()
    if not title_conf:
        return 'A WA-based site.'
    return title_conf.value

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
                    get_title(),
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
        ('用户管理', admin.get_url('users')),
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


def make_main_basic():
    return ui.main(
        form(
            rawtext('网站名称:'),
            input_(
                type='text',
                name='site_title',
                placeholder=get_title(),
                # klass='form-control',
            ),
            input_(
                type='submit',
                value='确定',
            ),
            action=admin.get_url('update_site_title'),
            method='post',
        ),
        klass='col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2'
    )


@admin.get('/config', name='config')
@view
def config():
    h = make_head(title(get_title()))
    mid = ui.container_fluid(
        ui.row(
            make_sidebar('基本配置'),
            make_main_basic(),
        )
    )
    return ui.page(h, body(make_header(), mid))


@admin.post('/update_site_title', name='update_site_title')
def update_site_title(db):
    new_title = request.forms['site_title']
    title_conf = db.query(ConfigTable).filter_by(key='site_title').first()
    if not title_conf:
        db.add(ConfigTable('site_title', new_title))
    else:
        title_conf.value = new_title
        db.flush()
    redirect(admin.get_url('config'), 303)


@admin.get('/users', name='users')
@view
def users_():
    h = make_head(title(get_title()))
    mid = ui.container_fluid(
        ui.row(
            make_sidebar('用户管理'),
            users.make_admin_main(),
        )
    )
    return ui.page(h, body(make_header(), mid))

@admin.get('/', name='home')
@view
def home():
    return h2('hello, world.')


def init():
    admin.install(plugin)
    return admin
