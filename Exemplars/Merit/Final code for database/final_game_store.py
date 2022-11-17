#Imports
import sqlite3
from final_functions import *
DATABASE_FILE = "game_store_database.db" 

#Main code
with sqlite3.connect(DATABASE_FILE) as connection:   
    print("Welcome to the Game Store Data Base")
    status_check = input("Are you a developer or customer? \nd for developer (Developer has access to everything )\nc for customer (Customer can only view product table)\n")
    #the code will be usable for both a developer and a user
        
    try:
        status_check = str.lower(status_check)
        if status_check == "d": 
            while True:
                #creates an infinite loop 
                option = input("\nWelcome Developer\n\n\nWhat would you like to access? \na for add\nd for delete\nu for update\ns for show\ne for escape \n\n\n")
                   #allows for the user to select what they want to do to the database
                try:
                    option = str.lower(option)
                            #human proofing for capitilization of inputs
                    if option == "a":
                        add_option = input("What table would you like to add into? \np = product \nu = user \n")
                        try:
                            add_option = str.lower(add_option)
                            if add_option == "p":
                                show_product_general(connection)
                                add_product(connection,input("What is the name? "),input("What is the age_rating? "),input("What is the price? "),input("What is the description? "),input("What is the genre? "),input("What is the game_rating? "))   
                                    #asks for reuqired variables in the add product function                 
                            elif add_option == "u":
                                show_user(connection)
                                add_user(connection, input("What is the first_name? "), input("What is the surname? "), input("What is the phone_number? "), input("What is the email address? "))
                                    #asks for the required variables for the add user function
                        except:
                            print("Failed to select a correct variable\n\n")

                    elif option == "d":
                        table =  input("Which table would you like to delete from?\np for product\nu for user\ns for sales\n")
                        try:
                            str.lower(table) 
                            if table == "p":
                                show_product_general(connection)
                                y = "DELETE FROM product WHERE product_id = ?"
                                    #statement that deletes a product ID and all the data from that row if selected
                            elif table == "u":
                                show_user(connection)
                                y = "DELETE FROM user WHERE user_id = ?"
                                    #statement that deletes a user ID and all the data from that row if selected
                            elif table == "s":
                                show_sales(connection)
                                y = "DELETE FROM sales WHERE sales_id = ?"
                                    #statement that deletes a sales ID and all the data from that row if selected
                            else:
                                print("Invalid input")
                                    #Tells you if something is inputed inccorectly
                        except:
                            print("Please input the table from which you would like to delete a row from using the letters as shown\n")
                        sql = y
                        delete_an_item_id = input("What item would you like to delete? (please use the id)  \n")
                        delete_item(connection, table , delete_an_item_id,sql,)
                            #asking what table and item ID they would like to delete
                    elif option == "u":
                        update(connection, input("What table would you like to update?\nu = user\np = product\n") ) 
                            #asks what they table they would like to update  
                    elif option == "s":
                        options_show(connection)
                            #shows the table of products
                    elif option == "e":
                        print("\n\nGoodbye!!\n\n\n\n")
                        break
                            #if the user wants to exit they may                      
                except:
                    print("Not a valid input\n\n")
                        #the user has not inputed a usable input such as a number which cannot be a lower string
        if status_check == "c":
            while True:
                #creates an infinite loop 
                cust_option = input("\nWelcome Customer\n\nWhat would you like to do?\np for price ascending or descending \ne for escape\n")
                try:
                    cust_option = str.lower(cust_option)
                    if cust_option == "p":
                        show_product(connection)
                            #Initiates the show product function
                    elif cust_option == "e":
                        print("\n\nGoodbye!!\n\n\n\n")
                        break
                except:
                    print("Invalid input, try choosing a letter")
                        #explains the problem
    except:
        print("Try selecting a valid input as letter s or p")        