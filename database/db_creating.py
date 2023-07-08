import logging
import os
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
cwd = os.getcwd()
db_path = os.path.join(cwd, 'database', 'reserved.db')

""" Database configuration """
async_engine = create_async_engine(f"sqlite+aiosqlite:///{db_path}",
                                   echo=True,
                                   future=True)
Base = declarative_base()


class Client(Base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True)
    name = Column(String(128))
    phone_number = Column(String(32))
    gmt = Column(String(64))
    comment = Column(String)


class Question(Base):
    __tablename__ = 'questions'

    question_id = Column(Integer, primary_key=True)
    question = Column(String)
    name = Column(String(128))
    phone_number = Column(String(32))


class Meeting(Base):
    __tablename__ = 'meetings'

    client_id = Column(Integer, primary_key=True)
    full_name = Column(String(256))
    phone_number = Column(String(32))


class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    naming = Column(String)
    place = Column(String)
    date = Column(String(128))
    time = Column(String(32))
    price = Column(String(32))


async def base_start():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
