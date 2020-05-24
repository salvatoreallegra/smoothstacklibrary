import mysql.connector
from dbconnect import DBConn


def getAllLibraries():
    conn = DBConn()
    cnx = conn.getConnection()
    myCursor = cnx.cursor()
    libraryList = []
    myCursor.execute("SELECT branchName FROM tbl_library_branch")
    myresult = myCursor.fetchall()
    for x in myresult:
        libraryList.append(x)
    return libraryList
