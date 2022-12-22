#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__=='__main__':
    mydb = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1], 
                           passwd=argv[2], 
                           db=argv[3])
mycursor = mydb.cursor()
mycursor.execute("SELECT *FROM states")
mydb = mycursor.fetchall()
for x in mydb:
    print(x)
mycursor.close()
mydb.close()
