#!/usr/bin/python3
'''
This module defines a class with a
city base
'''

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Cities class that inherits from Base."""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
