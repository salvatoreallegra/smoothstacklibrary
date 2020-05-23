from library import *


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
        print("Add Book")
    elif choice == 2:
        print("Update Book")
    elif choice == 3:
        print("Delete Book")
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
        print("Add Book")
    elif choice == 2:
        print("Update Book")
    elif choice == 3:
        print("Delete Book")
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
        print("Add Book")
    elif choice == 2:
        print("Update Book")
    elif choice == 3:
        print("Delete Book")
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
        print("Add Borrow")
    elif choice == 2:
        print("Update Borrow")
    elif choice == 3:
        print("Delete Borrow")
    elif choice == 4:
        display_admin_menu()
    elif choice == 5:
        main()
    else:
        print("Invalid Selection")
        display_admin_menu_authors()


def display_admin_menu_override_due_date():
    choice = 0
    print("Override a Borrowers Due Date, Please Select Option Below...")
    print("1) Override Due Date")
    print("2) Back to Admin Functions")
    print("3) Return to Main Menu")

    choice = int(input("Enter Selection "))
    if choice == 1:
        print("Add Borrow")
    elif choice == 2:
        display_admin_menu()
    elif choice == 3:
        main()
    else:
        print("Invalid Selection")
        display_admin_menu_override_due_date()
