# -*- coding:utf-8 -*-

from bottle import Bottle

from .html import *
from . import ui

admin = Bottle()

def make_menu():
    return [
        a('Dashboard', href='#'),
        a('Dashboard', href='#'),
        a('Dashboard', href='#'),
        a('Dashboard', href='#'),
    ]

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
            div(
                ul(
                    *map(li, make_menu()),
                    klass='nav navbar-nav navbar-right'
                ),
                klass='navbar-collapse collapse'
            )
        ),
        role='navigation',
        klass="navbar navbar-inverse navbar-fixed-top"
    )
    return header


def make_sidebar():
    sidebar = ui.sidebar(klass='col-sm-3 col-md-2')
    sidebar(
        ul(
            *map(li, make_menu()),
            klass='nav nav-sidebar'
        ),
    )
    return sidebar

@admin.route('/')
def home():
    h = head()(
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
        title('test'),
    )
    mid = ui.container_fluid(
        ui.row(
            make_sidebar(),
            ui.main(
                h2('hello, world.'),
                klass='col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2'
            )
        )
    )
    return ui.page(h, body(make_header(), mid))


def init():
    return admin