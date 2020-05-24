from borrowerqueries import *
from librarianqueries import getAllLibraries

def display_borrower_menu():
    while(True):
        print("1) Check out a book")
        print("2) Return a Book")
        print("3) Quit to Previous")
        choice = int(input("Enter Your Selection: "))
        if choice == 1:
            display_borrower_checkout_menu()
        elif choice == 3:
            break
        else:
            print('Invalid Choice Try Again')

def display_borrower_checkout_menu():
    libraryList = []
    cardNum = int(input('Enter Your CardNumber: '))
    if cardNum == -1:
        return
    elif (cardIsValid(cardNum)):

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
            elif choice == i:
                break
            else:
                print("Invalid Choice Try Again")
    else:
        print('Invalid card number')
        print('Try again or enter -1 to return to previous menu')

def display_borrower_book_menu(branchName, cardNum):

    bookList = getListOfBooksFromBranch(branchName)
    bookIdList = []

    if bookList is None:
        print('No books for branch in DB')
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
