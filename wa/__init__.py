# -*- coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals, division

from functools import wraps, partial

import bottle

__version__ = (0, 1, 1, 'dev', 0)
__all__ = ('Error',
           'init',
           'route',
           'view',
)


def route(route_func, *a, **kw):
    '''
    把函数名作为 `route()` 的 `name` 参数实参，方便后续调用 app.get_url()。
    自动应用 `view()` 函数适配 wa.html.E 对象渲染。
    '''

    def _(f):
        if 'name' not in kw:
            kw['name'] = f.__name__
        apply = kw.get('apply', None)
        if apply:
            apply = bottle.makelist(apply)
            apply.append(view)
        else:
            apply = [view]
        kw['apply'] = apply
        t = route_func(*a, **kw)
        return t(f)

    return _


def view(f):
    @wraps(f)
    def _(*a, **kw):
        print a, kw
        return str(f(*a, **kw))
    return _


class Error(StandardError):
    pass


@bottle.hook('before_request')
def _setup_session():
    bottle.request.session = bottle.request.environ['beaker.session']


def init(conf=None):
    app = bottle.default_app()
    if conf:
        app.config.update(conf)

    # first of all, create db.
    from . import database
    from .apps import model

    database.init(app)

    # init admin
    from .apps import admin, users

    app.mount('/admin', admin.init())
    app.mount('/users', users.init())

    # init beaker
    import beaker.middleware

    session_opts = {
        'session.type': 'file',
        'session.data_dir': './session/',
        'session.auto': True,
    }
    app = beaker.middleware.SessionMiddleware(app, session_opts)

    # return app
    return partial(bottle.run, app=app)
