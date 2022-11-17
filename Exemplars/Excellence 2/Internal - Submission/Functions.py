'''File for all my functions'''

#Imports
import sqlite3

#Database connection
DATABASE_FILE = "MCU Characters.db"

def login(pword):
    '''Login so you can do more than just read the database'''
    user_input = input("Please input password:\n- ")
    if user_input == pword:
        print("\nLogin success! Welcome back QuirkyFish123\n\n")
        return True
    else:
        print("Incorrect password. Login failed.")
        return False


def show_characters():
    '''Reads and prints all IDs, names and alter-egos in the "Characters" table in the database'''
    #Connect to the database
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    #Read items
    cursor.execute("SELECT id, Name, Alter_ego FROM Characters;")
    results = cursor.fetchall()
    #Format into a nice-looking table
    print("="*70)
    print(f"| {'ID':<3}| {'Name':<30}| {'Alter-ego':<30}|")
    print("|" + "-"*68 + "|")
    #Print all items in organised rows and columns
    for item in results:
        print(f"| {item[0]:<3}| {item[1]:<30}| {item[2]:<30}|")
    print("="*70)
    #Close connection to make more efficient
    connection.close()


def show_powers():
    '''Reads and prints all IDs and power names in the "Powers" table in the database'''
    #Connect to the database
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    #Read items
    cursor.execute("SELECT * FROM Powers;")
    results = cursor.fetchall()
    #Format into a nice-looking table
    print("="*33)
    print(f"| {'ID':<3}| {'Power':<25}|")
    print("|" + "-"*31 + "|")
    #Print all items in organised rows and columns
    for item in results:
        print(f"| {item[0]:<3}| {item[1]:<25}|")
    print("="*33)
    #Close connection to make more efficient
    connection.close()


def update():
    '''Changes an entry of an existing item'''
    #invalid characters
    invalid1 = "'"
    invalid2 = '"'
    #Connects to database
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    show_characters()
    #Loop until a valid ID is input
    while True:
        #Makes the code not crash!
        try:
            character_id = input("\nWhich character do you want to update?\nPlease input character ID: ")
            if character_id == "//":
                break
            else:
                character_id = int(character_id)
            #Checks if an item with that ID exists
            cursor.execute("SELECT Name, Alter_ego FROM Characters WHERE id = ?;", (character_id,))
            test = cursor.fetchall()
            #If test is empty, ask again. Else break the loop and continue.
            if not test:
                print("That is not a valid ID. Please enter a valid ID.\n")
            else:
                break
        except:
            print("That is not a valid ID. Please enter a valid ID.\n")
    print("\nInformation on the character:\n")
    print_one_character(character_id)
    print(f"\nEach column will show up, type in the new entry.\nInvalid characters: {invalid1} {invalid2}\nIf you do not wish to change this information, type '//' and it will skip.")
    #Name
    while True:
        try:
            name = str(input("Name: "))
            if name == "//":
                break
            else:
                cursor.execute("UPDATE Characters SET Name = ? WHERE id = ?;", (name, character_id,))
                connection.commit()
                break
        except:
            print("You used an invalid character. Please try again.")
    #Alter-ego
    while True:
        try:
            alter_ego = str(input("Alter-ego: "))
            if alter_ego == "//":
                break
            else:
                cursor.execute("UPDATE Characters SET Alter_ego = ? WHERE id = ?;", (alter_ego, character_id,))
                connection.commit()
                break
        except:
            print("You used an invalid character. Please try again.")
    #Backstory
    print("Current backstory:")
    cursor.execute("SELECT Backstory FROM Characters WHERE id = ?;", (character_id,))
    current_backstory = cursor.fetchall()
    print(current_backstory)
    while True:
        try:
            backstory = str(input("Backstory: "))
            if backstory == "//":
                break
            else:
                cursor.execute("UPDATE Characters SET Backstory = ? WHERE id = ?;", (backstory, character_id,))
                connection.commit()
                break
        except:
            print("You used an invalid character. Please try again.")
    #Powers
    power_change = input("Would you like to update the powers? Y/N\n- ")
    if power_change == "Y":
        delete_powers(character_id)
        show_powers()
        print("Type the ID of each power this character has, including those already listed.\nIf the power you want is not on the list, type ADD\nWhen you have selected all the powers the character has type '//'.")
        while True:
            power_id = input("- ")
            if power_id == "//":
                break
            elif power_id == "ADD":
                create_power()
                show_powers()
            else:
                while True:
                    try:
                        power_id = int(power_id)
                        add_power(character_id, power_id)
                        break
                    except:
                        print("Please input a number")
                connection.commit()
    else:
        print("Powers remain the same")
    connection.close()


def delete_character():
    '''Deletes all information about a character'''
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    show_characters()
    while True:
        while True:
            character_id = input("Which character would you like to delete? If you do not wish to delete a character, type //\n\nPlease input character ID: ")
            if character_id == "//":
                break
            else:
                try:
                    character_id = int(character_id)
                    break
                except:
                    print("Please input a number")
        try:
            cursor.execute("DELETE FROM Characters WHERE id = ?;", (character_id,))
            connection.commit()
            delete_powers(character_id)
            break
        except:
            print("Invalid ID, please try again")
    connection.close()


def delete_powers(character_id):
    '''Delete all information on powers a character has'''
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Character_powers WHERE Character_id = ?;", (character_id,))
    connection.commit()
    connection.close()


def add_character():
    '''Adds a character into the "Characters" table in the MCU Characters database'''
    #Connect to the database
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    print("If you want to cancel, type //\n")
    #to simplify the loops
    is_it_empty = 0
    loop_again = True #If the character is complete, this will be false and won't loop again
    #Asks the user for information on the new character
    while loop_again == True:
        #Name
        #Instead of a messy while True loop
        while is_it_empty < 1:
            name = input("What is the character's (hero) name?\n- ")
            #They cancel
            if name == "//":
                is_it_empty = 1
            #They leave it empty
            elif not name:
                print("Please write a name")
            #They put something in
            else:
                is_it_empty = 1
        is_it_empty = 0 #resets the counter
        #Alter-ego
        while is_it_empty < 1:
            alter_ego = input("\nWhat is their alter-ego?\n- ")
            if alter_ego == "//":
                is_it_empty = 1
            elif not alter_ego:
                print("Please write an alter-ego")
            else:
                is_it_empty = 1
        is_it_empty = 0 #resets the counter
        #backstory
        while is_it_empty < 1:
            backstory = input("\n What is their backstory? Keep it short and simple.\n- ")
            if backstory == "//":
                is_it_empty = 1
            elif not backstory:
                print("Please write a backstory")
            else:
                is_it_empty = 1
        #Insert new item into table
        cursor.execute("INSERT INTO Characters (Name, Alter_ego, Backstory) VALUES (?,?,?);", (name, alter_ego, backstory,))
        #Commit changes, it creates an ID and then I can add powers using said ID
        connection.commit()
        cursor.execute("SELECT id FROM Characters WHERE Name = ?;", (name,))
        character_id = cursor.fetchone() #Stores the ID in a variable
        character_id = character_id[0] #Isolates the ID from the tuple
        show_powers() #so the user can see available powers
        print("Please type the ID of every power this character has.\nIf a power doesn't yet exist, type ADD.\nWhen done, type //.")
        power_count = 0 #to check if the user input nothing
        #loop as many times as needed to get all powers
        while loop_again == True:
            power_id = input("Power ID: ")
            if power_id == "ADD":
                create_power()
                show_powers()
            elif power_id == "//":
                #if nothing added, adds "No Powers" automatically
                if power_count < 1:
                    add_power(character_id, 15)
                    loop_again = False
                else:
                    loop_again = False
            else:
                try:
                    power_id = int(power_id)
                    #Check if that power exists
                    cursor.execute("SELECT id FROM Powers WHERE id = ?;", (power_id,))
                    check = cursor.fetchall()
                    if not check:
                        print("That is not a valid ID")
                    else:
                        add_power(character_id, power_id)
                        power_count += 1
                except:
                    print("That is not a valid ID")
        #Commit changes
        connection.commit()
        connection.close()
        show_characters()


def add_power(character_id, power_id):
    '''Adds a power to a character in the Character_powers table'''
    #Connect to the database
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    #Insert new item into table
    cursor.execute("INSERT INTO Character_powers (Character_id, Power_id) VALUES (?,?);", (character_id, power_id,))
    #Commit changes
    connection.commit()
    connection.close()


def create_power():
    '''Creates a new power'''
    #Connect to database
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    #asks to name new power, then checks if it already exists
    new_power = input("Name the new power: ")
    cursor.execute("SELECT Power FROM Powers WHERE Power = ?;", (new_power,))
    check = cursor.fetchall()
    #if it doesn't exist, it gets made. else you dont make it.
    if not check:
        cursor.execute("INSERT INTO Powers (Power) VALUES (?);", (new_power,))
        connection.commit()
    else:
        print("That power already exists")
    connection.close()


def print_one_character(character_id):
    '''Prints all information on one character'''
    power_num = 0
    #Connect to database
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    #Collects all information on the intended character
    cursor.execute("SELECT Characters.Name, Characters.Alter_ego, Powers.Power, Characters.Backstory FROM Characters JOIN Character_powers ON Characters.id = Character_powers.Character_id JOIN Powers ON Powers.id = Character_powers.Power_id WHERE Characters.id = ?;", (character_id,))
    results = cursor.fetchall()
    individual_result = results[0]
    print(f"\nName:\n{individual_result[0]}, AKA {individual_result[1]}")
    print("-"*50)
    #If there is only one row
    if len(results) == 1:
        print(f"Powers:\n{results[0][2]}")
    else:
        print("Powers:")
        #For multiple powers
        for amount in results:
            #To change between the powers
            individual_result = results[power_num]
            #Print the power
            print(individual_result[2])
            power_num += 1
    print("-"*50)
    #Backstory
    print(f"Backstory:\n{results[0][3]}")
    connection.close()


def logged_in_menu(account):
    '''Menu for when user is logged in'''
    while account == True:
        #asks for user input
        print("\n")
        print("What would you like to do? Input number for action.")
        print("1. Create new character")
        print("2. Show all characters")
        print("3. Show all powers")
        print("4. Show all information on one character")
        print("5. Update a character")
        print("6. Delete a character")
        print("7. Logout")
        print("8. End")
        while True:
            #loop until an integer is put in
            while True:
                try:
                    user_input = int(input("- "))
                    print()
                    break
                except:
                    print("That is not a valid option")
            if user_input == 1: #make new character
                add_character()
                break
            elif user_input == 2: #show all characters
                show_characters()
                break
            elif user_input == 3: #Show powers
                show_powers()
                break
            elif user_input == 4: #show one character
                show_characters()
                while True:
                    try:
                        character = int(input("\nWhich character would you like to see? Input their ID.\n- "))
                        print_one_character(character)
                        break
                    except:
                        print("That is not a valid character ID")
                break
            elif user_input == 5: #update a character
                update()
                break
            elif user_input == 6: #delete character
                delete_character()
                break
            elif user_input == 7: #logout
                account = False
                print("\nLogout successful")
                return account
            elif user_input == 8: #end program
                return "end"
            else:
                print("That is not a valid option")


def guest_menu(account):
    '''Menu when logged out'''
    pword = "fish"
    while account == False:
        #asks for user input
        print("\n")
        print("What would you like to do? Input number for action.")
        print("1. Show all characters")
        print("2. Show all powers")
        print("3. Show all information on one character")
        print("4. Login")
        print("5. End")
        while True:
            #loop until an integer is put in
            while True:
                try:
                    user_input = int(input("- "))
                    print()
                    break
                except:
                    print("That is not a valid option")
            if user_input == 1: #print characters
                show_characters()
                break
            elif user_input == 2: #print powers
                show_powers()
                break
            elif user_input == 3: #show one character
                show_characters()
                while True:
                    try:
                        character = int(input("\nWhich character would you like to see? Input their ID.\n- "))
                        print_one_character(character)
                        break
                    except:
                        print("That is not a valid character ID")
                break
            elif user_input == 4: #Login
                account = login(pword)
                return account
            elif user_input == 5: #end program
                return "end"
            else:
                print("That is not a valid option")