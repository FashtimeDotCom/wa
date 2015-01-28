# -*- coding:utf-8 -*-

import uuid
import hashlib
import datetime

from sqlalchemy import Column, String, Integer, Sequence, DateTime

from ..database import Model


class Config(Model):
    __tablename__ = 'config'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    key = Column(String(50), nullable=False)
    value = Column(String(50))

    def __init__(self, key, value):
        self.key = key
        self.value = value


class Users(Model):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    salt = Column(String(8), nullable=False)
    register_time = Column(DateTime(timezone=True), nullable=False)

    @staticmethod
    def make_password(salt, password):
        return hashlib.sha1(salt + password).hexdigest()

    def __init__(self, username, password):
        self.username = username
        self.salt = uuid.uuid4().get_hex()[:8]
        self.password = self.make_password(self.salt, password)
        self.register_time = datetime.datetime.now()

    def check_password(self, password):
        return self.password == self.make_password(self.salt, password)
