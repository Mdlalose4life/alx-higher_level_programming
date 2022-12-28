#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""


from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
    passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    db = cur.fetchall()
    for row in db:
        print(row)
    cursor.close()
    db.close()
