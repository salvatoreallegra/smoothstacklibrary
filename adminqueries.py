import mysql.connector
from dbconnect import DBConn

conn = DBConn()
cnx = conn.getConnection()
myCursor = cnx.cursor()

# Get all borrowers from library database


#####################################################
# All Functions for Books and Authors
#####################################################

def getAllBooksAndAuthors():
    query = ("SELECT b.bookId, b.title, a.authorName "
             "FROM library.tbl_book as b "
             "INNER JOIN tbl_book_authors ba on ba.bookId = b.bookId "
             "INNER JOIN tbl_author a on ba.authorId = a.authorId ")

    myCursor.execute(query)

    for (bookId, title, authorName) in myCursor:
        print("Book Id", "Book Title", "Author Name")
        print(bookId, title, authorName)
        print("")

    if cnx.is_connected():
        print('still connected')
    cnx.commit()


def addBookAndAuthor(bookId):
    args = [bookId]
    myCursor.callproc(
        'add_new_book_and_author', args)
    myCursor.execute()
    cnx.commit()
    print('Book and Author Added Successfully...')


def updateBook(bookId):
    args = [bookId]
    myCursor.callproc(
        'update_book', args)
    myCursor.execute()
    cnx.commit()
    print('Book Updated Successfully...')


def deleteBook(bookId):
    args = [bookId]
    myCursor.callproc(
        'delete_book', args)
    myCursor.execute()
    cnx.commit()
    print('Book has been deleted successfully...')


def updateAuthor(authorId):
    args = [authorId]
    myCursor.callproc(
        'update_author', args)
    myCursor.execute()
    cnx.commit()
    print('Author has been updated successfully...')


def deleteAuthor(authorId):
    args = [authorId]
    myCursor.callproc(
        'delete_author', args)
    myCursor.execute()
    cnx.commit()
    print('Author has been deleted successfully...')


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
