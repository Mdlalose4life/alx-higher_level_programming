#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`
"""

import MySQLdb
from sys import argv

"""
Access to the database and find states
that start with N.
"""

if __name__ == '__main__':
    con = MySQLdb.connect(host="localhost", port=3306,
    user=argv[1], passwd=argv[2], db=argv[3])
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")
    for row in cur.fetchall():
        print(row)