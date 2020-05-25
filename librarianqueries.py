# Ian Agostini 05/23/20
import mysql.connector
from dbconnect import DBConn


conn = DBConn()
cnx = conn.getConnection()

crsr = cnx.cursor()


def get_branch_names():
    print("This is get_branch_names")
    sql_command03 = """SELECT branchName, branchAddress
            FROM  tbl_library_branch
            """
    crsr.execute(sql_command03)
    branch_names = crsr.fetchall()
    return branch_names


def get_branch_id_by_name(branch):
    sql_command0 = """SELECT branchId
                  FROM tbl_library_branch
                  WHERE branchName = '""" + str(branch) + """'
                  """
    crsr.execute(sql_command0)  # we need to get branch id as branchName is subject to change
    branch_id = crsr.fetchall()  # stores all fetched data in 'branch_id'
    return branch_id


def get_branch_name_by_id(branch_id):
    sql_command0 = """SELECT branchName
                FROM tbl_library_branch
                WHERE branchId = '""" + str(branch_id[0][0]) + """'
                """
    crsr.execute(sql_command0)  # gets the name of the branch
    branch = crsr.fetchall()  # stores all fetched data in 'branch'
    return branch


def update_branch_name(select, branch_id):
    sql_command1 = """UPDATE tbl_library_branch
            SET branchName = '""" + str(select) + """'
            WHERE branchId = '""" + str(branch_id[0][0]) + """'
            """  # will use variable 'branch_id', 'select'
    crsr.execute(sql_command1)


def update_branch_desc(select, branch_id):
    sql_command2 = """UPDATE tbl_library_branch
          SET branchAddress = '""" + str(select) + """'
          WHERE branchId = '""" + str(branch_id[0][0]) + """'
          """  # will use variable 'branch_id', 'select'
    crsr.execute(sql_command2)


def get_book_names_by_branch_id(branch_id):
    sql_command01 = """SELECT title, noOfCopies
        FROM (((tbl_book_authors NATURAL JOIN tbl_book)
        NATURAL JOIN tbl_library_branch)
        NATURAL JOIN tbl_book_copies)
        WHERE branchId = '""" + str(branch_id[0][0]) + """'
        """
    crsr.execute(sql_command01)
    book_names = crsr.fetchall()  # get the names of all the books
    return book_names


def get_book_id_by_name(title):
    sql_command33 = """SELECT bookId
                    FROM tbl_book
                    WHERE title = '""" + str(title) + """'
                    """
    crsr.execute(sql_command33)
    book_id = crsr.fetchall()
    return book_id


def get_num_of_copies_by_book_id_and_branch_id(book_id, branch_id):
    # Code to get num of requested books at the branch
    sql_command4 = """SELECT noOfCopies
            FROM ( (TBL_BOOK NATURAL JOIN TBL_BOOK_COPIES ) NATURAL JOIN TBL_LIBRARY_BRANCH )
            WHERE bookId='""" + str(book_id[0][0]) + """"'
            AND branchId='""" + str(branch_id[0][0]) + """"'
            """
    crsr.execute(sql_command4)
    num_copies = crsr.fetchall()  # stores all fetched data in 'num_copies'
    return num_copies


def update_book_copies(nom_books, book_id, branch_id):
    sql_command4 = """UPDATE tbl_book_copies
            SET noOfCopies = '""" + str(nom_books) + """'
            WHERE bookId='""" + str(book_id[0][0]) + """'
            AND branchId='""" + str(branch_id[0][0]) + """'
            """
    crsr.execute(sql_command4)







def getAllLibraries():
    conn = DBConn()
    cnx = conn.getConnection()
    myCursor = cnx.cursor()
    libraryList = []
    myCursor.execute("SELECT branchName FROM tbl_library_branch")
    myresult = myCursor.fetchall()
    for x in myresult:
        libraryList.append(x)
    return libraryList

