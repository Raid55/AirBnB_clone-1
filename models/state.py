#!/usr/bin/python3
'''
    Implementation of the State class
'''

from os import getenv

from models.city import City
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='delete')
    else:
        @property
        def cities(self):
            obj_dict = models.storage.all(City)
            return [v for k, v in obj_dict.items() if v.state_id == self.id]
