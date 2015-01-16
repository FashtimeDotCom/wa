# -*- coding:utf-8 -*-

from bottle import Bottle

from .html import *
from . import ui

admin = Bottle()


def make_header():
    header = div(**{'class': 'page-header'})
    header.h1('Welcome to admin page.')
    return header


def make_sidebar():
    # with div() as sidebar:
    # with dl('功能1'):
    #         dd('菜单1')
    #         dd('菜单2')
    #     with dl('功能2'):
    #         dd('菜单1')
    #         dd('菜单2')
    # return sidebar
    sidebar = ui.sidebar(**{'class':'col-sm-3 col-md-2'})
    sidebar.i('sidebar')
    return sidebar


def make_footer():
    return ui.footer()(i('This is a footer.'))


@admin.route('/')
def home():
    h = head()(
        script(
            src=r'http://cdn.bootcss.com/bootstrap/3.3.0/js/bootstrap.min.js',
        ),
        link(rel='stylesheet',
             href=r'http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css',
        ),
        title('test'),
    )
    b = body()(
        make_header(),
        make_sidebar(),
        ui.container()(
            h2('Hello, world!'),
            rawtext(r'''
            <div class="list-group">
                <a href="#" class="list-group-item">Dapibus ac facilisis in</a>
                <div class="list-group">
                  <a href="#" class="list-group-item active">
                    Cras justo odio
                  </a>
                  <a href="#" class="list-group-item">Dapibus ac facilisis in</a>
                  <a href="#" class="list-group-item">Morbi leo risus</a>
                  <a href="#" class="list-group-item">Porta ac consectetur ac</a>
                  <a href="#" class="list-group-item">Vestibulum at eros</a>
                </div>
                <a href="#" class="list-group-item">Dapibus ac facilisis in</a>
                <div class="list-group">
                  <a href="#" class="list-group-item active">
                    Cras justo odio
                  </a>
                  <a href="#" class="list-group-item">Dapibus ac facilisis in</a>
                  <a href="#" class="list-group-item">Morbi leo risus</a>
                  <a href="#" class="list-group-item">Porta ac consectetur ac</a>
                  <a href="#" class="list-group-item">Vestibulum at eros</a>
                </div>
                <div class="list-group">
                  <a href="#" class="list-group-item active">
                    Cras justo odio
                  </a>
                  <a href="#" class="list-group-item">Dapibus ac facilisis in</a>
                  <a href="#" class="list-group-item">Morbi leo risus</a>
                  <a href="#" class="list-group-item">Porta ac consectetur ac</a>
                  <a href="#" class="list-group-item">Vestibulum at eros</a>
                </div>
            </div>
            '''
            )),
        hr(),
        make_footer(),
    )
    return ui.page(h, b)


def init():
    return admin