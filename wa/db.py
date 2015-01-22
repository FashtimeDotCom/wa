# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, Sequence

from bottle.ext import sqlalchemy as bs

Base = declarative_base()

app = None

def make_session():
    global app
    if not app:
        raise
    


def init(app):
    engine = create_engine(app.config['sqlalchemyuri'], echo=True)
    plugin = bs.Plugin(
        engine,
        Base.metadata,
        create=True,
    )
    app.install(plugin)

class Config(Base):
    __tablename__ = 'config'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    key = Column(String(50))
    value = Column(String(50))
    def __init__(self):
        pass