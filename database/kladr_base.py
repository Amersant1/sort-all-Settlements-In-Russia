from typing import Any
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from posixpath import abspath
from os.path import join

from controller import engine, Base, Session


class Settlement(Base):
    """
    
    Модель данных о кнопке в посте

    Id : int
    Name - название города(str)
    Latitude - широта(float)
    Longitude - долгота(float)
    KladrIndex- index в кладре

    """

    __tablename__ = 'Settlements'
    
    Id = Column(Integer, nullable=False, unique=True, primary_key=True)
    Name = Column(String, nullable=False)
    Latitude = Column(Float,nullable=True)
    Longitude = Column(Float, nullable=True)
    KladrIndex=Column(Integer)
    Type=Column(String)

def add_to_base(Name,Latitude,Longitude,KladrIndex,Type):
    settlement=Settlement(Name=Name,
                          Latitude=Latitude,
                          Longitude=Longitude,
                          KladrIndex=KladrIndex,
                          Type=Type)
    Session.add(settlement)
    Session.commit()
    return 0

def make_session():
    session=sessionmaker(engine)()
    return session
# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
