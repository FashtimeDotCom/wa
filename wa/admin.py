# -*- coding:utf-8 -*-

from bottle import Bottle

from .html import *

admin = Bottle()

def make_header():
    with div(id='header', **{'class':'navbar-header'}) as header:
        header.h1('Welcome to admin page.')
    return header

def make_sidebar():
    with div() as sidebar:
        with dl('功能1'):
            dd('菜单1')
            dd('菜单2')
        with dl('功能2'):
            dd('菜单1')
            dd('菜单2')
    return sidebar

def make_footer():
    with div() as footer:
        i('This is a footer.')
    return footer

@admin.route('/')
def test():
    with html(lang='zh-cn') as doc:
        with head():
            script(
                src=r'http://cdn.bootcss.com/bootstrap/3.3.0/js/bootstrap.min.js',
            )
            link(rel='stylesheet',
                 href=r'http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css',
                 )
            title('test')
        with body():
            make_header()
            hr()
            make_sidebar()
            content = div()
            content.h2('Hello, world!')
            hr()
            make_footer()
    return doc


def init():
    return admin