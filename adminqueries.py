import mysql.connector
from dbconnect import DBConn

conn = DBConn()
cnx = conn.getConnection()
myCursor = cnx.cursor()

# Get all borrowers from library database


def getAllBorrowersWithBooksDue():

    query = ("SELECT name, title, dueDate "
             "FROM tbl_borrower "
             "Inner Join tbl_book_loans on tbl_borrower.cardNo = tbl_book_loans.cardNo "
             "Inner join tbl_book on tbl_book_loans.bookId = tbl_book.bookId "
             "Where dueDate > curdate();")

    myCursor.execute(query)

    for (name, title, dueDate) in myCursor:
        print(name, title, dueDate)

    # myCursor.callproc('get_book_loans')

    # for result in myCursor.stored_results():
    #     print(result.fetchall())
    if cnx.is_connected():
        print('still connected')
    cnx.commit()
    # myCursor.execute("SELECT * FROM tbl_borrower")
    # myresult = myCursor.fetchall()
    # for x in myresult:
    #     print(x)
