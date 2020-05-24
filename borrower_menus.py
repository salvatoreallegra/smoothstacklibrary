from borrowerqueries import *
from librarianqueries import getAllLibraries

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
                libraryList.append(x[0])
                print(f"{i}) {x[0]}")
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
