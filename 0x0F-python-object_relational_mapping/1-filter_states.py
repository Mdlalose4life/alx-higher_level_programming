#!/usr/bin/python3
"""
This script lists all states with a `name` starting with
the letter `N` from the database `hbtn_0e_0_usa`
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':

    mydb = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])

    cur = mydb.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
            ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    mydb.close()
