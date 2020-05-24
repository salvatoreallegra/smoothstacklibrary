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

# def lib2():
#     sql_command03 = """SELECT branchName, branchAddress
#         FROM  tbl_library_branch
#         """
#     crsr.execute(sql_command03)
#     branch_names = crsr.fetchall()
#
#     # print("The list of branches are: " + str(menu11))
#
#
#     print()
#     print("Which Branch do you manage?:")
#
#     menu1 = [item[0] for item in branch_names]
#     menu1.append("Quit to previous")
#     for x in range(len(menu1)):
#         print('\t', x+1, '. ', menu1[x])
#
#     select = input("")
#     branch = ""
#     if 0 < int(select) < int(len(menu1)):
#         branch = menu1[int(select)-1]
#     elif int(select) == len(menu1):
#         print("PlaceHolderExit")  # takes user back to main menu
#     else:
#         print("Invalid Selection")
#
#     sql_command0 = """SELECT branchId
#               FROM tbl_library_branch
#               WHERE branchName = '""" + str(branch) + """'
#               """
#     crsr.execute(sql_command0)  # we need to get branch id as branchName is subject to change
#     branch_id = crsr.fetchall()  # stores all fetched data in 'branch_id'
#     lib3(branch_id)  # calls on the sub menu, giving it the branch_id so it know which to edit
#
#
# def lib3(branch_id):  # sub menu where user can edit number of copies of a book or change branch name
#     print()
#     print("What would you like to do?:")
#     menu2 = ["Update the details of the Library", "Add copies of Book to the Branch", "Quit to previous"]
#     for x in range(len(menu2)):  # prints the menu
#         print('\t', x+1, '. ', menu2[x])
#     select = input("")
#
#     sql_command0 = """SELECT branchName
#             FROM tbl_library_branch
#             WHERE branchId = '""" + str(branch_id[0][0]) + """'
#             """
#     crsr.execute(sql_command0)  # gets the name of the branch
#     branch = crsr.fetchall()  # stores all fetched data in 'branch'
#
#     if select == '1':  # if they want to change library details
#         update_library_details(branch, branch_id)
#     elif select == '2':  # if they want to change number of copies of a book
#         add_copies_of_book(branch, branch_id)
#     elif select == '3':  # if the user wants to go back to the previous menu
#         lib2()
#     else:
#         print("Invalid Selection")
#
#
# def update_library_details(b, branch_id):  # method for changing the name & desc of the branch
#
#     sql_command0 = """SELECT branchName
#         FROM tbl_library_branch
#         WHERE branchId = '""" + str(branch_id[0][0]) + """'
#         """
#     crsr.execute(sql_command0)
#     branch_name = crsr.fetchall()  # stores all fetched data in 'branch_id'
#     b = branch_name[0][0]  # branch name is stores as [(ExampleName,)] so I need get get the value from the array/list
#     print()
#     print("You have chosen to update the Branch with Branch Id: " + str(branch_id[0][0]) + " and Branch Name: " +
#           str(b))
#     print("Enter ‘quit’ at any prompt to cancel operation.")
#     select = input("Please enter new branch name or enter N/A for no change:")
#
#     if select == "N/A" or select == "":  # if user decides they want the field left the same
#         print("")
#     elif select == "quit":  # if the user typed 'quit'
#         lib3(branch_id)
#     else:  # updates the branch name with what the user typed
#         sql_command1 = """UPDATE tbl_library_branch
#         SET branchName = '""" + str(select) + """'
#         WHERE branchId = '""" + str(branch_id[0][0]) + """'
#         """  # will use variable 'branch_id', 'select'
#         crsr.execute(sql_command1)
#
#     select = input("Please enter new branch address or enter N/A for no change:")
#     if select == "N/A" or select == "":  # if user decides they want the field left the same
#         print("")
#     elif select == "quit":
#         lib3(branch_id)
#     else:  # updates the branch's desc
#         sql_command2 = """UPDATE tbl_library_branch
#         SET branchAddress = '"""+str(select) + """'
#         WHERE branchId = '""" + str(branch_id[0][0]) + """'
#         """  # will use variable 'branch_id', 'select'
#         crsr.execute(sql_command2)
#     print("Successfully Updated")  # could add an actual checker to see if it works.....
#
#     crsr.execute(sql_command0)  # gets the current value of branchName
#     branch_name = crsr.fetchall()  # stores that value
#     print("Branch name is now '" + str(branch_name[0][0]) + "'")
#
#     lib3(branch_id)  # takes user back to lib3 selection screen
#
#
# def add_copies_of_book(b, branch_id):  # Can probably remove the 'b' variable
#     sql_command0 = """SELECT branchName
#            FROM tbl_library_branch
#            WHERE branchId = '""" + str(branch_id[0][0]) + """'
#            """
#     crsr.execute(sql_command0)
#     branch_name = crsr.fetchall()
#     # b = branch_name[0][0]
#
#     sql_command01 = """SELECT title, noOfCopies
#     FROM (((tbl_book_authors NATURAL JOIN tbl_book)
#     NATURAL JOIN tbl_library_branch)
#     NATURAL JOIN tbl_book_copies)
#     WHERE branchId = '""" + str(branch_id[0][0]) + """'
#     """
#     crsr.execute(sql_command01)
#     book_names = crsr.fetchall()  # get the names of all the books
#     #print("The list of books are: "+str(book_names[0][0]))
#
#     print()
#     print("Pick the Book you want to add copies of, to your branch:")
#
#     menu3 = [item[0] for item in book_names]
#     menu3.append("Quit to previous")
#     for x in range(len(menu3)):  # prints a menu of all the books plus the 'quit to previous' option
#         print('\t', x + 1, '. ', menu3[x])
#     select = input("")
#     if 0 < int(select) < int(len(menu3)):  # where the user selects which book they want
#         title = menu3[int(select)-1]
#
#         sql_command33 = """SELECT bookId
#                 FROM tbl_book
#                 WHERE title = '""" + str(title) + """'
#                 """
#         crsr.execute(sql_command33)
#         book_id = crsr.fetchall()
#
#         # Code to get num of requested books at the branch
#         sql_command4 = """SELECT noOfCopies
#         FROM ( (TBL_BOOK NATURAL JOIN TBL_BOOK_COPIES ) NATURAL JOIN TBL_LIBRARY_BRANCH )
#         WHERE bookId='"""+str(book_id[0][0])+""""'
#         AND branchId='"""+str(branch_id[0][0])+""""'
#         """
#         crsr.execute(sql_command4)
#         num_copies = crsr.fetchall()  # stores all fetched data in 'num_copies'
#         print("Existing number of copies of "+str(title)+": "+str(num_copies[0][0]))  # informs user of how many copies
#         select = input("Enter new number of copies:")
#         # ToDo: Code to make sure input is a valid int
#
#         nom_books = int(select)
#         # Code updating num of copies at branch
#         sql_command4 = """UPDATE tbl_book_copies
#         SET noOfCopies = '"""+str(nom_books)+"""'
#         WHERE bookId='"""+str(book_id[0][0])+"""'
#         AND branchId='"""+str(branch_id[0][0])+"""'
#         """
#         crsr.execute(sql_command4)
#         print("Successfully Updated Copies")  # could add an actual checker to see if it works.....
#         lib3(branch_id)  # takes user back to lib3 selection screen
#
#     elif int(select) == int(len(menu3)):  # if the user selected to go back
#         lib3(branch_id)
#     else:
#         print("Invalid Selection")
#
#
# lib2()