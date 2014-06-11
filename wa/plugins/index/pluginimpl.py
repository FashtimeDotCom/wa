# -*- coding:utf-8 -*-
from flask import Blueprint

from wa.plugin import PluginInterface

index = Blueprint('index', __name__,
        template_folder='templates')

@index.route('/')
def page():
    return '''<html><h1>Hello, WA!</h1></html>'''

class PluginImpl(PluginInterface):
    def __init__(self, config):
        PluginInterface.__init__(self, config)

#    def blueprints(self):
#        return [
#                (index, {'url_prefix':'/index'}),
#                ]

    def index_blueprint(self):
        return (index, {})


