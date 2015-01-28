# -*- coding:utf-8 -*-
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from bottle.ext import sqlalchemy as bs


Model = declarative_base()

plugin = None
create_session = None

def init(app):
    global plugin, create_session
    engine = create_engine(app.config['sqlalchemyuri'], echo=True)
    create_session = sessionmaker(bind=engine)
    # print Base.metadata.tables
    Model.metadata.create_all(bind=engine)
    plugin = bs.Plugin(
        engine,
        Model.metadata,
    )
    app.install(plugin)
