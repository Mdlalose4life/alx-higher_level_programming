#!/usr/bin/python3
"""
Script that lists all lists all `State`
objects from the database `Alx-Holberton`.
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from model_state import Base, State


if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

    url = {'drivername': 'mysql+mysqldb', 'host': 'localhost',
           'username': mySQL_u, 'password': mySQL_p, 'database': db_name}

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    x = session.query(State).order_by(State.id).all()

    for instance in x:
        print("{}: {}".format(instance.id, instance.name))
    session.close()