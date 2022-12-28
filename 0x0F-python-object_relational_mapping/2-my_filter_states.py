#!/usr/bin/python3
"""
a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

"""
Access to the database and find state that
Matches the given name.
"""

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
    user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    
    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY"\
            " '{:s}' ORDER BY states.id ASC".format(argv[4]))

    for x in cursor.fetchall():
        if x[1] == argv[4]:
            print(x)
