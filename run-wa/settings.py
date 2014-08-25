#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from os.path import dirname, realpath

here = dirname(realpath(__file__))

DEBUG = True

SECRET_KEY = '4807a8ed-bcb9-4a20-9b5c-591c2d112f40'

HOST = '0.0.0.0'
PORT = 5000


DB_HOST = 'localhost'
DB_PORT =  3306
DB_USERNAME = 'root'
DB_PASSWORD = ''
DB_DATABASE = 'wa'

UPLOADS_DIR = os.path.join(here, 'uploads')

WA_PLUGINS = {
#        ('watest', 'watest_index'),
        }

WA_INDEX_PLUGIN = None #('watest', 'watest_index')
WA_ADMIN_PLUGIN = ('wa', 'wa_admin')

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test_wa.db'

WA_ENTRY = ('wa', 'wa_admin')
