#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    mydb = MySQLdb.connect(host="localhost",
                           port=3306, passwd=argv[2], db=argv[3])
    
    cur = mydb.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    for row in cur.fetchall():
        print(row)
        