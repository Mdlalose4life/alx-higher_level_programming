import mysql.connector

mydb = mysql.connector.connect(host="localhost", 
user="sqluser", 
passwd="password", 
db=" hbtn_0e_0_usa")

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT *FROM states WHERE name='&name'")
for x in mycursor:
    print(x)