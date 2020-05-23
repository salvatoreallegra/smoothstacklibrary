import mysql.connector
from dbconnect import DBConn

conn = DBConn()
cnx = conn.getConnection()
myCursor = cnx.cursor()

# Get all borrowers from library database


#####################################################
# All Functions for Books and Authors
#####################################################


#####################################################
# All Functions for Publishers
#####################################################


#####################################################
# All Functions for Branches
#####################################################

#####################################################
# All Functions for Borrowers
#####################################################


#####################################################
# All Functions for Borrower Due Date
#####################################################

def getAllBorrowersWithBooksDue():

    query = ("SELECT tbl_book_loans.bookId as bookId, tbl_book_loans.cardNo as cardNo, name, title, dueDate "
             "FROM tbl_borrower "
             "Inner Join tbl_book_loans on tbl_borrower.cardNo = tbl_book_loans.cardNo "
             "Inner join tbl_book on tbl_book_loans.bookId = tbl_book.bookId "
             )

    myCursor.execute(query)

    for (bookId, cardNo, name, title, dueDate) in myCursor:
        print("Book Id", "Card #", "Borrower Name", "Book Name", "Due Date")
        print(bookId, cardNo, name, title, dueDate)
        print("")

    cnx.commit()


def updateDueDate(bookId, cardNo, newDueDate):
    args = [bookId, cardNo, newDueDate, 0]

    resultArgs = myCursor.callproc(
        'update_due_date', args)

    print(resultArgs[3])
    # myCursor.execute()

    # for result in myCursor.stored_results():
    #     print(result.fetchall())
    cnx.commit()
