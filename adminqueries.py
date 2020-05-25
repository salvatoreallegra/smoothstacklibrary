import mysql.connector
from dbconnect import DBConn

conn = DBConn()
cnx = conn.getConnection()

myCursor = cnx.cursor()
