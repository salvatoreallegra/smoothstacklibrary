from borrowerqueries import *
from librarianqueries import getAllLibraries

def display_borrower_menu():
    print('\n')
    try:
        cardNum = int(input('Enter Your CardNumber: '))
    except ValueError:
        print('\nInvalid entry: exiting to main.\n')
        return
    if (cardIsValid(cardNum)):
        print('\n')
        while(True):
            print("1) Check out a book")
            print("2) Return a Book")
            print("3) Quit to Previous")
            try:
                choice = int(input("Enter Your Selection: "))
            except ValueError:
                print('invalid choice')
                continue
            if choice == 1:
                display_borrower_checkout_menu(cardNum)
            elif choice == 2:
                display_borrower_return_menu(cardNum)
            elif choice == 3:
                break
            else:
                print('Invalid Choice Try Again')
    else:
        print('\nInvalid card number: exiting to main.\n')

def display_borrower_return_menu(cardNum):
    bookList = []
    result = getAllCheckedOutBooks(cardNum)
    if not result:
        print('\nNo Checked Out Books to Return\n')
        return
    while (True):
        i = 0
        for x in result:
            i += 1
            bookList.append(x[1])
            print(f"{i}) {x[0]}")
        print(f"{i+1}) Return to previous menu")
        # print(f"i:  {i}")
        try:
            choice = int(input('Pick the book you want to return: '))
            print('\n')
        except ValueError:
            print('Invalid Entry')
            continue
        if choice > 0 and choice <= len(bookList):
            checkBookBackIn(bookList[choice-1], cardNum)
            break
        elif choice == i + 1:
            break
        else:
            print("Invalid Choice Try Again")


def display_borrower_checkout_menu(cardNum):
    libraryList = []

    result = getAllLibraries()
    if result is None:
        print('No Branches in DB')
        return
    while (True):
        i = 0
        for x in result:
            i += 1
            libraryList.append(x[0])
            print(f"{i}) {x[0]}")
        print(f"{i+1}) Return to previous menu")
        choice = int(input('Pick the branch you want to check out from: '))
        if choice > 0 and choice <= len(libraryList):
            display_borrower_book_menu(libraryList[choice - 1], cardNum)
            break

        elif choice == i + 1:
            break
        else:
            print("Invalid Choice Try Again")


def display_borrower_book_menu(branchName, cardNum):

    bookList = getListOfBooksFromBranch(branchName, cardNum)
    bookIdList = []

    if not bookList:
        print('\nNo Books Availabe at this library retuning to previous menu\n')
        return
    while(True):
        i = 1
        print("Pick the Book you want to check out")
        for x in bookList:
            print(f"{i}) {x[0]}")
            bookIdList.append(x[1])

        print(f"{i+1}) Return to previous menu")
        choice = int(input('Choose book: '))
        if choice > 0 and choice <= len(bookIdList):
            addBookIntoBookLoans(bookIdList[choice-1], branchName, cardNum)
            break
        elif choice == i + 1:
            break
