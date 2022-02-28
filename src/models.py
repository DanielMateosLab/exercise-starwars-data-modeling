import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

class Favourite(Base):
    __tablename__ = 'favourite'
    id = Column(Integer, primary_key=True)
    kind = Column(String(20), nullable=False)
    # entity_id = Column(Integer, ForeignKey(kind + '.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False, unique=True)
    climate = Column(String(10), nullable=False)
    terrain = Column(String(10), nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False, unique=True)
    birthyear = Column(Integer, nullable=False)
    gender = Column(String(6), nullable=False)
    height = Column(Integer, nullable=False)
    homeplanet = Column(Integer, ForeignKey('planet.id'), nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')