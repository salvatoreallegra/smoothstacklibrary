import mysql.connector

from dbconnect import DBConn

conn = DBConn()
cnx = conn.getConnection()

myCursor = cnx.cursor()


def getAllLibrariesgit push():
    libraryList = []
    print("Hello Libraries")
    myCursor.execute("SELECT branchID, branchName FROM tbl_library_branch")
    myresult = myCursor.fetchall()
    for x in myresult:
        libraryList.append(x)
    return libraryList
