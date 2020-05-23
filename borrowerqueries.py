from dbconnect import DBConn

def cardIsValid(cardNum):
    conn = DBConn()
    cursor = conn.getCursor()
    cursor.execute(f"select name from tbl_borrower where cardNo = {cardNum}")
    if not cursor.fetchall():
        return False
    else:
        return True

def getListOfBooksFromBranch(branchName):
    conn = DBConn()
    cursor = conn.getCursor()
    cursor.execute(f"""
        select title  
        from tbl_book tb 
        inner join tbl_book_copies tbc 
        on tb.bookId = tbc.bookId 
        inner join tbl_library_branch tlb 
        on tlb.branchId = tbc.branchId
        where tlb.branchName = "{branchName}"
    """)
    return cursor.fetchall()

def addBookIntoBookLoans(bookName):
    pass

if __name__ == "__main__":
    print(checkIfCardIDValid('111'))
