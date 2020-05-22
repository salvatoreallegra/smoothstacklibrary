from librarianqueries import *
from adminqueries import *
from library_user_queries import *


MAIN_LIBRARIAN_CHOICE = 1
MAIN_ADMINISTRATOR_CHOICE = 2
MAIN_BORROWER_CHOICE = 3
QUIT_CHOICE = 4


def main():
    choice = 0
    while choice != QUIT_CHOICE:
        display_main_menu()
        choice = int(input('Enter your Selection: \n'))
        if choice == MAIN_LIBRARIAN_CHOICE:
            display_library1_menu()
        elif choice == MAIN_ADMINISTRATOR_CHOICE:
            print("Main Admin Choice\n")
        elif choice == MAIN_BORROWER_CHOICE:
            print("Main Borrower Choice\n")
        elif choice == QUIT_CHOICE:
            print('Exiting the program. . .\n')
        else:
            print('Error: invalid selection...\n')


def display_main_menu():
    print("---Welcome to the Smooth Stack Library Management System---")
    print("Which Category of User are You?")
    print("1) Librarian?")
    print("2) Administrator?")
    print("3) Borrower?")
    print("4) Quit")


def display_library_branches_menu():
    choice = 0
    menuItemNo = 1
    primaryKey = 0
    selectionPrimaryKeyDictionary = {}

    # Call getAllLibraries located in librarianqueries.py
    libraryList = getAllLibraries()
    for library in libraryList:
        # print out the second index in the list which will always be the library name
        print(str(menuItemNo) + " " + library[1])
        selectionPrimaryKeyDictionary[str(menuItemNo)] = library[0]
        menuItemNo = menuItemNo + 1
        print(selectionPrimaryKeyDictionary)

    choice = input("Enter Your Selection: ")

    # loop through map
    for x in selectionPrimaryKeyDictionary:
        if x == choice:
            primaryKey = selectionPrimaryKeyDictionary[x]

            print(primaryKey)


def display_library1_menu():
    choice = 0
    print("1) Enter the branch you manage")
    print("2) Return to main menu")
    choice = int(input('Enter Your Selection '))
    if choice == 1:
        print("Librarian SubMenu\n")
        display_library_branches_menu()
    elif choice == 2:
        main()
    else:
        print("Invalid Selection")
        display_library1_menu()


main()
