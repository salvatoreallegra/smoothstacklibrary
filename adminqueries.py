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

    try:
        query = ("SELECT b.title, a.authorName "
                 "FROM library.tbl_book as b "
                 "INNER JOIN tbl_book_authors ba on ba.bookId = b.bookId "
                 "INNER JOIN tbl_author a on ba.authorId = a.authorId ")

        myCursor.execute(query)

        for (title, authorName) in myCursor:
            print("Book Title......", "Author Name.....")
            print(title, authorName)
            print("")

        cnx.commit()
    except:
        print("Error getting books and authors, please re-enter data")


def getAllBooksAndAuthorsWithIds():

    try:
        query = ("SELECT b.bookId, b.title, a.authorId, a.authorName "
                 "FROM library.tbl_book as b "
                 "INNER JOIN tbl_book_authors ba on ba.bookId = b.bookId "
                 "INNER JOIN tbl_author a on ba.authorId = a.authorId ")

        myCursor.execute(query)

        for (bookId, title, authorId, authorName) in myCursor:
            print("Book Id ", "Book Title......",
                  "AuthorId ", "Author Name.....")
            print(bookId, title, authorId, authorName)
            print("")

        cnx.commit()
    except:
        print("Error getting books and authors, please re-enter data")


def addBookAndAuthor(bookName, authorName, publisherName):
    try:
        args = [authorName, bookName, publisherName]
        myCursor.callproc(
            'add_new_book_author', args)

        # myCursor.execute()
        cnx.commit()
    except mysql.connector.Error as err:
        print(err)


def updateBookAuthors(bookId, bookName, authorId, authorName):
    args = [bookId, bookName, authorId, authorName]
    try:
        myCursor.callproc(
            'update_book_author', args)
        cnx.commit()
        print('Book and Author updated Successfully')
    except mysql.connector.Error as err:
        print(err)


def deleteBookAuthors(bookId, authorId):
    args = [bookId, authorId]
    try:
        myCursor.callproc(
            'delete_book_author', args)
        cnx.commit()
        print('Book and Author updated Successfully')
    except mysql.connector.Error as err:
        print(err)


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

def getAllPublishers():
    query = ("select publisherId, publisherName, publisherAddress, publisherPhone"
             "from tbl_publisher")
    myCursor.execute(query)

    for (publisherId, publisherName, publisherAddress, publisherPhone) in myCursor:
        print("PublisherId", "Publisher Name",
              "Publisher Address", "Publisher Phone")
        print(publisherId, publisherName, publisherAddress, publisherPhone)
        print("")

    cnx.commit()


def addPublisher(pubName, pubAddress, pubPhone):
    try:
        args = [pubName, pubAddress, pubPhone, ]
        myCursor.callproc(
            'add_publisher', args)
        # myCursor.execute()
        cnx.commit()
        print('Publisher has been successfully added...')
        return True
    except mysql.connector.Error as err:
        print(err)
        return False


def updatePublisher(publisherId):
    try:
        args = [publisherId]
        myCursor.callproc(
            'update_publisher', args)
        cnx.commit()
    except mysql.connector.Error as err:
        print(err)


def deletePublisher():
    args = []
    myCursor.callproc(
        'delete_publisher', args)
    myCursor.execute()
    cnx.commit()

#####################################################
# All Functions for Branches
#####################################################


def getAllBranches():
    query = ("select branchId, branchName, branchAddress"
             "from tbl_library_branch")
    myCursor.execute(query)

    for (branchId, branchName, branchAddress) in myCursor:
        print("Branch Id", "Branch Name", "Branch Address")
        print(branchId, branchName, branchAddress)
        print("")

    cnx.commit()


def addBranch():
    args = []
    myCursor.callproc(
        'add_branch', args)
    myCursor.execute()
    cnx.commit()


def updateBranch():
    args = []
    myCursor.callproc(
        'update_branch', args)
    myCursor.execute()
    cnx.commit()


def deleteBranch():
    args = []
    myCursor.callproc(
        'delete_branch', args)
    myCursor.execute()
    cnx.commit()

#####################################################
# All Functions for Borrowers
#####################################################


def getAllBorrowers():
    query = ("select cardNo, name, address, phone "
             "from tbl_borrower")
    myCursor.execute(query)

    for (cardNo, name, address, phone) in myCursor:
        print("Card No", "Name", "Address", "Phone")
        print(cardNo, name, address, phone)
        print("")

    if cnx.is_connected():
        print('still connected')
    cnx.commit()


def addBorrower(cardNo, name, address, phone):
    try:
        args = [cardNo, name, address, phone]
        myCursor.callproc(
            'add_borrower', args)
        cnx.commit()
    except mysql.connector.Error as err:
        print(err)


def updateBorrower(cardNo, name, address, phone):
    try:
        args = [cardNo, name, address, phone]
        myCursor.callproc(
            'update_borrower', args)
        cnx.commit()
        print('Updated Successfully')
    except mysql.connector.Error as err:
        print(err)


def deleteBorrower(cardNo):
    try:
        args = [cardNo]
        myCursor.callproc(
            'delete_borrower', args)
        cnx.commit()
        print('deleted successfully')
    except mysql.connector.Error as err:
        print(err)

#####################################################
# All Functions for Borrower Due Date
#####################################################


def getAllBorrowersWithBooksDue():

    try:

        query = ("SELECT tbl_book_loans.bookId as bookId, tbl_book_loans.cardNo as cardNo, name, title, dueDate "
                 "FROM tbl_borrower "
                 "Inner Join tbl_book_loans on tbl_borrower.cardNo = tbl_book_loans.cardNo "
                 "Inner join tbl_book on tbl_book_loans.bookId = tbl_book.bookId "
                 )

        myCursor.execute(query)

        if(myCursor.fetchall):

            for (bookId, cardNo, name, title, dueDate) in myCursor:
                print("Book Id", "Card #", "Borrower Name",
                      "Book Name", "Due Date")
                print(bookId, cardNo, name, title, dueDate)
                print("")
            return True

        else:
            return False

    except:
        print("Could not get borrowers with Books Due")

    finally:
        cnx.commit()


def updateDueDate(bookId, cardNo, newDueDate):

    try:
        args = [bookId, cardNo, newDueDate, ]

        resultArgs = myCursor.callproc(
            'update_due_date', args)
        print("Due Date Updated Successfully")
        # count = count = int(myCursor.rowcount)
        # print(str("Row Count"), count)
        # if count == 0:
        #     print("No records where updated, re-enter data..")
        cnx.commit()
    except mysql.connector.Error as err:
        print(err)


    # print(resultArgs[3])
if __name__ == "__main__":
    authorExists("Stephan King")
