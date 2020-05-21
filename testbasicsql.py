import mysql.connector

from dbconnect import DBConn

conn = DBConn()
cnx = conn.getConnection()

myCursor = cnx.cursor()

myCursor.execute("SELECT * FROM tbl_book")

myresult = myCursor.fetchall()

for x in myresult:
    print(x)
