import mysql.connector

from dbconnect import DBConn


try:
    conn = DBConn()
    cnx = conn.getConnection()
    myCursor = cnx.cursor()

    args = [1, 'Shady Hollow', 'WunderBar']
    result_args = myCursor.callproc(
        'PROC_UPDATE_LIBRARY_BRANCH', args)

    # for result in myCursor.stored_results():
    #     print(result.fetchall())


except:
    print("Error executing stored procedure")

finally:
    myCursor.close()
    conn.close()
