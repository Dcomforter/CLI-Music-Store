# This is a command-line interface music store
from functions import login
from functions import userMenu

# Prints message for main menu
def mainMessage():
    print("\n\tWelcome to Dcomforter's Music Store")
    print("\n<=========== List of Commands ========================>\n")
    print("Login\t\t-\t Log In User/Create an account")
    print("Exit\t\t-\t Exit the program\n")

# The program starts from here
def main():
    mainMessage()

    # Initialize variables
    logged_in = False
    curr_user = ""

    while not logged_in:
        
        command = input(">> ").lower()
        
        if command == "login":
            logged_in, curr_user = login()
            if logged_in:
                userMenu(curr_user)
                logged_in = False
                mainMessage()
            else:
                mainMessage()
            
        elif command == "exit":
            print("\nThanks for using this program.\n")
            break
        else:
            print("\nWrong input, kindly choose from LOGIN or EXIT. ")
            mainMessage()

if __name__ == '__main__':
    main()
