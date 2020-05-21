
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
            print("Librarian Choice\n")
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


main()
