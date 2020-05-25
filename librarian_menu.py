# Ian Agostini 05/24/20
import mysql.connector
from librarianqueries import *

from dbconnect import DBConn

conn = DBConn()
cnx = conn.getConnection()

crsr = cnx.cursor()


def lib2():

    branch_names = get_branch_names()

    print()
    print("Which Branch do you manage?:")

    menu1 = [item[0] for item in branch_names]
    menu1.append("Quit to previous")
    for x in range(len(menu1)):
        print('\t', x+1, '. ', menu1[x])

    select = input("")
    branch = ""
    if 0 < int(select) < int(len(menu1)):
        branch = menu1[int(select)-1]
    elif int(select) == len(menu1):
        # print("PlaceHolderExit")  # takes user back to main menu
        return
    else:
        print("Invalid Selection")

    branch_id = get_branch_id_by_name(branch)
    # calls on the sub menu, giving it the branch_id so it know which to edit
    lib3(branch_id)


def lib3(branch_id):  # sub menu where user can edit number of copies of a book or change branch name
    print()
    print("What would you like to do?:")
    menu2 = ["Update the details of the Library",
             "Add copies of Book to the Branch", "Quit to previous"]
    for x in range(len(menu2)):  # prints the menu
        print('\t', x+1, '. ', menu2[x])
    select = input("")

    branch = get_branch_name_by_id(branch_id)

    if select == '1':  # if they want to change library details
        update_library_details(branch, branch_id)
    elif select == '2':  # if they want to change number of copies of a book
        add_copies_of_book(branch, branch_id)
    elif select == '3':  # if the user wants to go back to the previous menu
        lib2()
    else:
        print("Invalid Selection")


# method for changing the name & desc of the branch
def update_library_details(b, branch_id):

    branch_name = get_branch_name_by_id(branch_id)
    # branch name is stores as [(ExampleName,)] so I need get get the value from the array/list
    b = branch_name[0][0]
    print()
    print("You have chosen to update the Branch with Branch Id: " + str(branch_id[0][0]) + " and Branch Name: " +
          str(b))
    print("Enter ‘quit’ at any prompt to cancel operation.")
    select = input("Please enter new branch name or enter N/A for no change:")

    if select == "N/A" or select == "":  # if user decides they want the field left the same
        print("")
    elif select == "quit":  # if the user typed 'quit'
        lib3(branch_id)
    else:  # updates the branch name with what the user typed
        update_branch_name(select, branch_id)

    select = input(
        "Please enter new branch address or enter N/A for no change:")
    if select == "N/A" or select == "":  # if user decides they want the field left the same
        print("")
    elif select == "quit":
        lib3(branch_id)
    else:  # updates the branch's desc

        update_branch_desc(select, branch_id)
    # could add an actual checker to see if it works.....
    print("Successfully Updated")

    branch_name = get_branch_name_by_id(branch_id)
    print("Branch name is now '" + str(branch_name[0][0]) + "'")

    lib3(branch_id)  # takes user back to lib3 selection screen


def add_copies_of_book(b, branch_id):  # Can probably remove the 'b' variable

    branch_name = get_branch_name_by_id(branch_id)
    # b = branch_name[0][0]

    book_names = get_book_names_by_branch_id(branch_id)

    # print("The list of books are: "+str(book_names[0][0]))

    print()
    print("Pick the Book you want to add copies of, to your branch:")

    menu3 = [item[0] for item in book_names]
    menu3.append("Quit to previous")
    # prints a menu of all the books plus the 'quit to previous' option
    for x in range(len(menu3)):
        print('\t', x + 1, '. ', menu3[x])
    select = input("")
    if 0 < int(select) < int(len(menu3)):  # where the user selects which book they want
        title = menu3[int(select)-1]

        book_id = get_book_id_by_name(title)

        num_copies = get_num_of_copies_by_book_id_and_branch_id(
            book_id, branch_id)
        print("Existing number of copies of "+str(title)+": " +
              str(num_copies[0][0]))  # informs user of how many copies
        select = input("Enter new number of copies:")
        # ToDo: Code to make sure input is a valid int

        nom_books = int(select)
        update_book_copies(nom_books, book_id, branch_id)
        # could add an actual checker to see if it works.....
        print("Successfully Updated Copies")
        lib3(branch_id)  # takes user back to lib3 selection screen

    elif int(select) == int(len(menu3)):  # if the user selected to go back
        lib3(branch_id)
    else:
        print("Invalid Selection")

