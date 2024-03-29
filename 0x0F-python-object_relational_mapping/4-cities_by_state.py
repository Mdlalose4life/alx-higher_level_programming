#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the cities
    from the database.
    """

    mydb = MySQLdb.connect(host="localhost", port=3306,
                           passwd=argv[2], db=argv[3])

    with mydb.cursor() as cur:
        cur.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")

    if cur.fetchall() is not None:
        for row in cur.fetchall():
            print(row)
