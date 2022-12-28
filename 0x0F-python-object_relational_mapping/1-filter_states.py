#!/usr/bin/python3
"""
lists all states with starting name with N
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

"""
Access the database and retrive data on states
that statrs with later N
"""

if __name__ == '__main__':
    con = MySQLdb.connect(host="localhost", port=3306, 
    user=argv[1], passwd=argv[2], db=argv[3])
    cur = con.cur()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
            ORDER BY statte.id ASC")
    for x in cur.fetchall():
        print(x)
