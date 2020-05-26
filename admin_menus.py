from library import *
from adminqueries import *
from datetime import datetime


# Main Menu for Admin functions
def display_admin_menu():
    choice = 0
    print("Administration Main Menu, please select option below")
    print("1) Add/Update/Delete Book and Author")
    print("2) Add/Update/Delete Publishers")
    print("3) Add/Update/Delete Library Branches")
    print("4) Add/Update/Delete Borrowers")
    print("5) Override Due Date for Borrowers")
    print("6) Return to Main Menu")
    choice = int(input("Enter Selection "))
    if choice == 1:
        display_admin_menu_authors()
    elif choice == 2:
        display_admin_menu_publishers()
    elif choice == 3:
        display_admin_menu_branches()
    elif choice == 4:
        display_admin_menu_borrowers()
    elif choice == 5:
        display_admin_menu_override_due_date()
    elif choice == 6:
        main()
    else:
        print("Invalid Selection")
        display_admin_menu()


def display_admin_menu_authors():
    choice = 0
    print("Update Books and Authors, please select option below")
    print("1) Add Book and Author")
    print("2) Update Book and Author")
    print("3) Delete Book and Author")
    print("4) Back to Admin Functions")
    print("5) Return to Main Menu")

    choice = int(input("Enter Selection "))
    if choice == 1:
        print("Before entering a book and author, please enter the books publisher information ")
        publisherName = input("Enter Publishers Name ")
        publisherAddress = input("Enter Publishers Address ")
        publisherPhone = input("Publishers Phone # ")

        successfulAdd = addPublisher(
            publisherName, publisherAddress, publisherPhone)
        if successfulAdd == False:
            display_admin_menu_authors()

        print("Displaying Current Books and Authors")

        getAllBooksAndAuthors()
        bookName = input("Enter book name ")
        authorName = input("Enter author name ")
        publisherName = input("Enter publisher name ")
        addBookAndAuthor(bookName, authorName, publisherName)
        display_admin_menu_authors()

    elif choice == 2:
        getAllBooksAndAuthorsWithIds()
        bookId = int(input("Enter Book Id"))
        bookName = input("Enter new book Name ")
        authorId = int(input("Enter Author Id "))
        authorName = input("Entter new Author Name")
        updateBookAuthors(bookId, bookName, authorId, authorName)
        display_admin_menu_authors()
    elif choice == 3:
        getAllBooksAndAuthorsWithIds()
        bookId = int(input("Enter Book Id "))
        authorId = int(input("Enter Author Id "))
        deleteBookAuthors(bookId, authorId)
        display_admin_menu_authors()

    elif choice == 4:
        display_admin_menu()
    elif choice == 5:
        main()
    else:
        print("Invalid Selection")
        display_admin_menu_authors()


def display_admin_menu_publishers():
    choice = 0
    print("Update Publisher Info, Please Select Option Below...")
    print("1) Add Publisher")
    print("2) Update Publisher")
    print("3) Delete Publisher")
    print("4) Back to Admin Functions")
    print("5) Return to Main Menu")

    choice = int(input("Enter Selection "))
    if choice == 1:
        print("To add a publisher please add publishers name address and phone number ")
        name = input("Enter Publisher Name ")
        address = input("Enter Publisher Address ")
        phoneNumber = input("Enter Publisher Phone #")
        addPublisher(name, address, phoneNumber)
        display_admin_menu_authors()
    elif choice == 2:
        print("Displaying all publishers")
        getAllPublishers()
        pubId = int(input("Enter publisher Id "))
        pubName = input("Enter publisher name ")
        pubAddress = input("Enter publishers address ")
        pubPhone = input("Enter Publisher's phone number ")
        updatePublisher(pubId, pubName, pubAddress, pubPhone)
        #display_admin_menu_authors()



    elif choice == 3:
        print("Delete Book")
        getAllPublishers()
        pubId = int(
            input('Please enter the id number of the publisher you would like to delete... '))
        deletePublisher(pubId)



    elif choice == 4:
        display_admin_menu()
    elif choice == 5:
        main()
    else:
        print("Invalid Selection")
        display_admin_menu_authors()


def display_admin_menu_branches():
    choice = 0
    print("Update Branch Info, Please Select Option Below...")
    print("1) Add Branch")
    print("2) Update Branch")
    print("3) Delete Branch")
    print("4) Back to Admin Functions")
    print("5) Return to Main Menu")

    choice = int(input("Enter Selection "))
    if choice == 1:
        print('Adding a new Branch...')
        branchName = input('Please enter the new branch name... ')
        branchAddress = input('Please enter the new branch address... ')
        addBranch(branchName, branchAddress)
    elif choice == 2:
        print("Updating Book... ")
        getAllBranches()
        branchId = int(
            input('Please enter the branch id number you would like to change... '))
        branchName = input('Please enter the new branch name... ')
        branchAddress = input('Please enter the new branch address... ')
        updateBranch(branchId, branchName, branchAddress)
    elif choice == 3:
        print("Deleting Book...")
        getAllBranches()
        branchId = int(
            input('Please enter the id number of the branch you would like to delete... '))
        deleteBranch(branchId)
    elif choice == 4:
        display_admin_menu()
    elif choice == 5:
        main()
    else:
        print("Invalid Selection")
        display_admin_menu_authors()


def display_admin_menu_borrowers():
    choice = 0
    print("Update Borrower Info, Please Select Option Below...")
    print("1) Add Borrower")
    print("2) Update Borrower")
    print("3) Delete Borrower")
    print("4) Back to Admin Functions")
    print("5) Return to Main Menu")

    choice = int(input("Enter Selection "))

    if choice == 1:
        print("Adding a borrower... ")
        cardNo = int(
            input('Please input a card number for the user(3 numbers only)... '))
        name = input('Please input the borrowers name... ')
        address = input('Please input the borrowers address... ')
        phone = input(
            'Please input the borrowers phone number ###-###-####... ')
        addBorrower(cardNo, name, address, phone)

    elif choice == 2:
        print("Updating a  Borrower... ")
        getAllBorrowers()
        cardNo = int(
            input("Please input a card number for the user(3 numbers only)... "))
        name = input('Please input the borrowers name... ')
        address = input('Please input the borrowers address... ')
        phone = input(
            'Please input the borrowers phone number ###-###-####... ')
        updateBorrower(cardNo, name, address, phone)

    elif choice == 3:
        print('Deleting a Borrower... ')
        getAllBorrowers()
        cardNo = int(
            input("Please input a card number for the user(3 numbers only)... "))
        deleteBorrower(cardNo)

    elif choice == 4:
        display_admin_menu()
    elif choice == 5:
        main()
    else:
        print("Invalid Selection")
        display_admin_menu_authors()

#####################################################
# Menu to update due date
#####################################################


def display_admin_menu_override_due_date():
    choice = 0
    print("Override a Borrowers Due Date, Please Select Option Below...")
    print("1) Override Due Date")
    print("2) Back to Admin Functions")
    print("3) Return to Main Menu")

    choice = int(input("Enter Selection "))
    borrowerId = 0
    if choice == 1:
        print("Listing Borrowers...")
        getAllBorrowersWithBooksDue()
        bookId = int(input("Enter Book Id..."))
        cardNumber = int(input("Enter Card Number..."))
        newDueDate = input(
            "Enter New Due Date in format YYYY-MM-DD... ")
        format_str = '%Y-%m-%d'  # The format
        updateDate = datetime.strptime(newDueDate, format_str)
        updatedDate = updateDate.date()
        updateDueDate(bookId, cardNumber, updatedDate)
        display_admin_menu_override_due_date()
    elif choice == 2:
        display_admin_menu()
    elif choice == 3:
        main()
    else:
        print("Invalid Selection")
        display_admin_menu_override_due_date()
