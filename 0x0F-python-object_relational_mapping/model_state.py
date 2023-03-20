#!/usr/bin/python3
'''
python file that contains the class definition of a
State and an instance Base = declarative_base():
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import column, Integer, String

Base = declarative_base()


class State(Base):
    """State class that inherits from Base."""
    __tablename__ = 'states'
    id = column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = column(String(128), nullable=False)
