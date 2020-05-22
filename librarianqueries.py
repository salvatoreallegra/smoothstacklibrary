import sqlite3
# Ian Agostini 05/22/20

# connecting to the database
connection = sqlite3.connect("myTable.db")  # will have to place actual connection to ur table here

# cursor
crsr = connection.cursor()


def lib2():
    print()
    menu1 = ["1) University Library, Boston", "2) State Library, New York", "3) Federal Library, Washington DC",
        "4) County Library, McLean VA", "5) Quit to previous"]
    for x in range(len(menu1)):
        print('\t', x+1, '. ', menu1[x])

    select = input("Which Branch do you manage?: ")
    branch = ""
    if select == '1' or '2' or '3' or '4':
        branch = menu[int(select)-1]
        branch[3:]  # Removes the "#)" from the branch
    elif select == '5':
        print("PlaceHolderExit")
    else:
        print("Invalid Selection")
    lib3(branch)


def lib3(branch):
    menu2 = ["1) Update the details of the Library", "2) Add copies of Book to the Branch", "3) Quit to previous"]
    for x in range(len(menu2)):
        print('\t', x+1, '. ', menu2[x])
    select = input("What would you like to do?:")

    if select == '1':
        update_library_details(branch)
    elif select == '2':
        add_copies_of_book(branch)
    elif select == '3':
        print("PlaceHolderExit")
    else:
        print("Invalid Selection")


def update_library_details(b):
    print("You have chosen to update the Branch with Branch Id: X and Branch Name: " +
          str(b) + "Enter ‘quit’ at any prompt to cancel operation.")
    select = input("Please enter new branch name or enter N/A for no change:")

    # get branch id
    sql_command0="""SELECT branchId
    FROM tbl_library_branch
    WHERE branchName = '""" + str(b) + """'
    """
    crsr.execute(sql_command0)  # we need to get branch id as branchName is subject to change
    branch_id = crsr.fetchall()  # stores all fetched data in 'branch_id'

    if select == "N/A":
        print("DoesNothing")
    else:
        print("ChangeName")
        sql_command1 = """UPDATE tbl_library_branch
        SET branchAddress = '"""+str(select) + """'
        WHERE branchId = '""" + int(branch_id) + """'
        """  # will use variable 'branch_id', 'select'
        crsr.execute(sql_command1)

    select = input("Please enter new branch address or enter N/A for no change:")
    if select == "N/A":
        print("DoesNothing")
    else:
        print("ChangeDesc")
        sql_command2 = """UPDATE tbl_library_branch
        SET branchAddress = '"""+str(select) + """'
        WHERE branchId = '""" + int(branch_id) + """'
        """  # will use variable 'branch_id', 'select'
        crsr.execute(sql_command2)
    print("Successfully Updated")  # could add an actual checker to see if it works.....
    lib3(b)  # takes user back to lib3 selection screen


def add_copies_of_book(b):
    menu3 = ["1) Lost Tribe by Sidney Sheldon", "2) The Haunting by Stepehen King", "3) Microtrends by Mark Penn",
             "4) Quit to cancel operation"]
    select = input("Pick the Book you want to add copies of, to your branch:")
    if select == '1' or '2' or '3':
        title_full = menu3[int(select)-1]
        title_full[3:]
        title = menu3[int(select)-1]
        title[3:]  # Removes the "#)" from the book title
        title.split(' by')[0]  # get the title of the book
        author = menu3[int(select)-1]
        author.split(' by')[1]  # gets the author

        # Code to get num of requested books at the branch
        sql_command4 = """SELECT noOfCopies
        FROM ( (TBL_BOOK NATURAL JOIN TBL_BOOK_COPIES ) NATURAL JOIN TBL_LIBRARY_BRANCH )
        WHERE Title='"""+str(title)+""""'
        AND branchName='"""+str(b)+""""'
        """
        crsr.execute(sql_command4)  # will use variable 'b', 'title', 'author'
        num_copies = crsr.fetchall()  # stores all fetched data in 'num_copies'
        print("Existing number of copies of "+str(title_full)+": "+str(num_copies))
        select = input("Enter new number of copies:")
        # Code to make sure input is a valid int

        # Code updating num of copies at branch
        sql_command4 = """UPDATE noOfCopies
        FROM ( (TBL_BOOK NATURAL JOIN TBL_BOOK_COPIES ) NATURAL JOIN TBL_LIBRARY_BRANCH )
        SET noOfCopies = '"""+int(select)+"""'
        WHERE Title='"""+str(title)+""""'
        AND branchName='"""+str(b)+""""'
        """  # will use variable 'b', 'num_copies', 'title', 'author'
        crsr.execute(sql_command4)
        lib3(b)  # takes user back to lib3 selection screen

    elif select == '4':
        print("PlaceHolderExit")
    else:
        print("Invalid Selection")


lib2()