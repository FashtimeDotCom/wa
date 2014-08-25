# -*- coding:utf-8 -*-

class EntryInterface(object):
    def __init__(self, app):
        self.app = app

    def blueprints(self):
        '''
        Return all blueprints this entry contained.
        '''
        raise NotImplemented()