# -*- coding:utf-8 -*-

class EntryInterface(object):
    def __init__(self, config):
        self._config = config

    def blueprints(self):
        '''
        Return all blueprints this entry contained.
        '''
        raise NotImplemented()