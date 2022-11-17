#Imports
from Functions import logged_in_menu, guest_menu

#Variables
pword = "fish" #Sets the password as "fish"
account = False #Starts the code logged off

if __name__ == "__main__":
    while True:
        if account == "end": #End program
            break
        elif account == True: #Logged in
            account = logged_in_menu(account)
        else: #Logged out
            account = guest_menu(account)