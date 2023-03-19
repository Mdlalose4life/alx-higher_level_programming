#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == '__main__':

    mydb = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cu = mydb.cursor()
    cu.execute("SELECT * FROM states ORDER BY states.id")
    for rows in cu.fetchall():
        print(rows)
    cu.close()
    mydb.close()
