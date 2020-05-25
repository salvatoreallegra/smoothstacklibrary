from dbconnect import DBConn

def cardIsValid(cardNum):
    conn = DBConn()
    cursor = conn.getCursor()
    cursor.execute(f"select name from tbl_borrower where cardNo = {cardNum}")
    if not cursor.fetchall():
        return False
    else:
        return True

def checkBookBackIn(bookId, cardNum):
    conn = DBConn()
    cursor = conn.getCursor()
    cursor.callproc('CheckInBook', [bookId, cardNum, 0])
    conn.commit()

def getAllCheckedOutBooks(cardNum):
     conn = DBConn()
     cursor = conn.getCursor()
     cursor.execute(f"""
        select tb.title, tb.bookId
        from tbl_book tb 
        inner join tbl_book_loans tbl 
        on tbl.bookId = tb.bookId
        where tbl.cardNo = {cardNum} and (tbl.bookReturned = 'N' or tbl.bookReturned = 'n')
     """)
     return cursor.fetchall()

def getListOfBooksFromBranch(branchName, cardNum):
    conn = DBConn()
    cursor = conn.getCursor()
    cursor.execute(f"""
        select title, tb.bookId
        from tbl_book tb 
        inner join tbl_book_copies tbc 
        on tb.bookId = tbc.bookId 
        inner join tbl_library_branch tlb 
        on tlb.branchId = tbc.branchId
        where tlb.branchName = '{branchName}' and not tbc.bookId in (select bookId from tbl_book_loans where cardNo = {cardNum} and bookReturned = 'N')
    """)
    return cursor.fetchall()

def addBookIntoBookLoans(bookId, branchName, cardNum):
    conn = DBConn()
    cursor = conn.getCursor()
    args = [bookId, branchName, cardNum, 0]
    cursor.callproc('CheckOutBook', args)
    conn.commit()

if __name__ == "__main__":
    addBookIntoBookLoans(1, 'Sleepy Hollow Library', 111)

