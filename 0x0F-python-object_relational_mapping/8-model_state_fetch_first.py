#!/usr/bin/python3
"""
Script that prints the first `State` object from the database `Alx-holberton`.
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

    cl_instance = session.query(State).first()

    if cl_instance:
        print("{}: {}".format(cl_instance.id, cl_instance.name))
    else:
        print("Nothing")
    session.close()
