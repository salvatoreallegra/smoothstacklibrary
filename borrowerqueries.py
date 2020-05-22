from dbconnect import DBConn

def checkIfCardIDValid(cardNum):
    conn = DBConn()
    cursor = conn.getCursor()
    cursor.execute(f"select name from tbl_borrower where cardNo = {cardNum}")
    if not cursor.fetchall():
        return False
    else:
        return True

if __name__ == "__main__":
    print(checkIfCardIDValid('111'))
