#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    places = relationship('Place', backref='users', cascade='delete')
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    __tablename__ = "users"
