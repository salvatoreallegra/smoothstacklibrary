import mysql.connector

from dbconnect import DBConn


try:
    conn = DBConn()
    cnx = conn.getConnection()
    myCursor = cnx.cursor()

    args = ['1', 'Shady Hollow', 'WunderBar', ]
    myCursor.callproc(
        'PROC_UPDATE_LIBRARY_BRANCH', args)

    # for result in myCursor.stored_results():
    #     print(result.fetchall())

    if cnx.is_connected():
        print('still connected')

    cnx.commit()


except:
    print("Error executing stored procedure")

finally:
    myCursor.close()
