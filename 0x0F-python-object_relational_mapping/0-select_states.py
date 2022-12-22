#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__=='__main__':
    mydb = MySQLdb.connect(host="localhost", 
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
