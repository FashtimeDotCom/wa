# -*- coding: utf-8 -*-
from .html import *

import bottle

__all__ = ['init']

import pkg_resources

class AppFinder(object):
    def __init__(self, group, name=None):
        self._group = group
        self._name = name

    def all_plugins(self, filter=None):
        if filter:
            for i in pkg_resources.iter_entry_points(self._group, self._name):
                if filter(i):
                    yield i.load()
        else:
            for i in pkg_resources.iter_entry_points(self._group, self._name):
                print i
                yield i.load()

    def plugin(self, prj, name):
        return pkg_resources.load_entry_point(prj, self._group, name)

def _load_app():
    pass


def init(conf=None):
    app = bottle.default_app()
    if conf:
        app.config.update(conf)

    # init admin
    from .admin import init as admin_init
    admin = admin_init()

    app.mount('/admin', admin)

    return app


class App(bottle.Bottle):
    def __init__(self, *a, **kw):
        Bottle.__init__(self, *a, **kw)
    #
    # def init_plugins(self):
    #     pf = PluginFinder(group='wa.plugin')
    #     # install plugins
    #     self._plugins = []
    #     for prj, plugin in self.config['WA_PLUGINS']:
    #         print prj, plugin
    #         plg = self._install_plugin(pf, prj, plugin)
    #         for bp, reg_args in plg.blueprints():
    #             self.register_blueprint(bp, **reg_args)
    #     # install index plugin
    #     if self.config['WA_INDEX_PLUGIN']:
    #         plg = self._install_plugin(pf, *self.config['WA_INDEX_PLUGIN'])
    #         bp, reg_args = plg.index_blueprint()
    #         self.register_blueprint(bp, **reg_args)
    #     # install admin plugin
    #     if self.config['WA_ADMIN_PLUGIN']:
    #         plg = self._install_plugin(pf, *self.config['WA_ADMIN_PLUGIN'])
    #         bp, reg_args = plg.admin_blueprint()
    #         self.register_blueprint(bp, **reg_args)
    #
    # def _install_plugin(self, pf, prj, plugin=None):
    #     plugin_class = pf.plugin(prj, plugin)
    #     if not plugin_class:
    #         print 'Plugin(%s) is not found in project(%s).'%(plugin, prj)
    #         return
    #     plg = plugin_class(self.config)
    #     self._plugins.append(plg)
    #     return plg

    # def load_wa_entry(self):
    #     pf = PluginFinder(group='wa.entry')
    #     prj, plugin = self.config['WA_ENTRY']
    #     wa_entry = pf.plugin(prj, plugin)
    #     if not wa_entry:
    #         raise wa.Error('Entry(%s) is not found in project(%s).'%(plugin, prj))
    #
    #     plg = wa_entry(self)
    #     for bp, reg_args in plg.blueprints():
    #         self.register_blueprint(bp, **reg_args)




app = bottle.default_app()

@app.route('/')
def test():
    with html() as doc:
        title('test')
        with body():
            adiv = div()
            adiv.h1('Hello, world!')
    return doc