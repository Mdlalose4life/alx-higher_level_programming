#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`
"""
import MySQLdb
import sys


if __name__ == '__main__':
    
    con = MySQLdb.connect(host="localhost", port=3306,
                        user=sys.argv[1], passwd=sys.argv[2], 
                        db=sys.argv[3], charset="utf8")
    cur = con.cursor()
    cur.execute(" ".join("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY id ASC"))
    for row in cur.fetchall():
        print(row)
    cur.close()
    con.close()
