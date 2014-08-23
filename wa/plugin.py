# -*- coding:utf-8 -*-

class PluginInterface(object):
    def __init__(self, config):
        self._config = config

    def blueprints(self):
        '''
        Return all blueprints this plugin contained.
        '''
        raise NotImplemented()

    def index_blueprints(self):
        '''
        Return a blueprint which can be use to render index page.
        If this plugin has not a index blueprint, return None.
        '''
        raise NotImplemented()

    def admin_blueprints(self):
        '''
        Return a blueprint which can be use to render amdin page.
        If this plugin has not a admin blueprint, return None.
        '''
        raise NotImplemented()

