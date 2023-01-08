#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys

"""
Access to the database and get the states
from the database.
"""


if __name__ == "__main__":

    con = MySQLdb.connect(
        host="localhost",port=3306, user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], charset="utf8")
    cu = con.cursor()
    cu.execute("SELECT * FROM states ORDER BY states.id")
    for row in cu.fetchall():
        print(row)
    cu.close()
    db.close()
