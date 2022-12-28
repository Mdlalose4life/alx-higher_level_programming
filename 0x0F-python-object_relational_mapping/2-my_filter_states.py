#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and find state that
    Matches the given name.
    """
    conn = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{:s}' ORDER BY \
                        states.id ASC".format(argv[4]))

    for x in cur.fetchall():
        print(x)