#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], charset="utf8")

    cu = db.cursor()
    cu.execute("SELECT * FROM states ORDER BY states.id")
    for rows in cu.fetchall():
        print(rows)
    cu.close()
    db.close()
