#!/usr/bin/python3


import MySQLdb
from sys import argv

'''
a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa.
'''
if __name__ == "__main__":
    cont = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = cont.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE"
            " '{:s}' ORDER BY id ASC".format(argv[4]))
    db = cursor.fetchall()
    for x in db:
        if x[1] == argv[4]:
            print(x)
