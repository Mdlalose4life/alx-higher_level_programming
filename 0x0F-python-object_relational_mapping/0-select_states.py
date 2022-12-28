#!/usr/bin/python3

import MySQLdb
from sys import argv

'''
a script that lists all states from the database hbtn_0e_0_usa
'''
if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost", port=3306, user="root",
        passwd="root", database"my_db", charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    my_db = cur.fetchall()
    for i in db:
        print(i)
    cursor.close()
    db.close()
