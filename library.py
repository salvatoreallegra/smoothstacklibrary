from librarianqueries import *
from adminqueries import *
from borrowerqueries import *
from admin_menus import *

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
            display_admin_menu()
        elif choice == MAIN_BORROWER_CHOICE:
            display_borrower_menu()
        elif choice == QUIT_CHOICE:
            print('Exiting the program. . .\n')
            break
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


def display_borrower_menu():
    print("1) Check out a book")
    print("2) Return a Book")
    print("3) Quit to Previous")
    choice = int(input("Enter Your Selection: "))
    if choice == 1:
        display_borrower_checkout_menu()
    else:
        print('Invalid Choice Try Again')



def display_borrower_checkout_menu():
    libraryList = []

    cardNum = int(input('Enter Your CardNumber: '))
    if cardNum == -1:
        return
    elif (cardIsValid(cardNum)):
        i = 0
        result = getAllLibraries()
        if result == None:
            return
        while (True):
            for x in result:
                i += 1
                libraryList.append(x[1])
                print(f"{i}) {x[1]}")
            print(f"{i+1}) Return to previous menu")
            choice = int(input('Pick the branch you want to check out from: '))
            print(f"choice: {choice}")
            if choice > 0 and choice <= len(libraryList):
                display_borrower_book_menu(libraryList[choice - 1])
                break
            elif choice == i:
                display_borrower_menu()
                break
            else:
                print("Invalid Choice Try Again")
    else:
        print('Invalid card number')
        print('Try again or enter -1 to return to previous menu')



def display_borrower_book_menu(branchName):
    bookList = getListOfBooksFromBranch(branchName)
    print("Pick the Book you want to check out")
    i = 1
    for x in bookList:
        print(f"{i}) {x[0]}")
        i += 1


if __name__ == "__main__":
    main()
