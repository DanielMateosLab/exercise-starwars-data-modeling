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

class Character_Favourites(Base):
    __tablename__ = 'character_favourites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    character = relationship(Character)


class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False, unique=True)
    model = Column(String(40), nullable=False, unique=True)
	manufacturer = Column(String(40), nullable=False, unique=True)
	crew = Column(Integer, nullable=False)
	passengers = Column(Integer, nullable=False)

class Starship_Favourites(Base):
    __tablename__ = 'starship_favourites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    starship_id = Column(Integer, ForeignKey('startship.id'), nullable=False)
    starship = relationship(Starship)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')