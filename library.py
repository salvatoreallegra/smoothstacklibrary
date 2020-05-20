print("Hello library")



def displayMainMenu():
    print("---Welcome to the Smooth Stack Library Management System---")
    print("Which Category of User are You?")
    print("1) Librarian?")
    print("2) Administrator?")
    print("1) Borrower?")
    menuSelection = input("Input 1, 2 or 3 ")
    return menuSelection


menuSelection = displayMainMenu()

print(menuSelection)
