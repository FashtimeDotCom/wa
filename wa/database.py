# -*- coding:utf-8 -*-
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, Sequence

from bottle.ext import sqlalchemy as bs


Base = declarative_base()

plugin = None
create_session = None

class Config(Base):
    __tablename__ = 'config'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    key = Column(String(50))
    value = Column(String(50))

    def __init__(self, key, value):
        self.key = key
        self.value = value

def init(app):
    global plugin, create_session
    engine = create_engine(app.config['sqlalchemyuri'], echo=True)
    create_session = sessionmaker(bind=engine)
    # print Base.metadata.tables
    Base.metadata.create_all(bind=engine)
    plugin = bs.Plugin(
        engine,
        Base.metadata,
    )
    app.install(plugin)
