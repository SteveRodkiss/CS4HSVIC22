#FUNCTIONS


#SHOW FUNCTIONS


def show_product(connection):
    try:
        cursor = connection.cursor()
        asc_or_desc = input("Price Ascending or Descending? (a or d) \n") 
            #asks for an input for ascending or descending price
        try: 
                #Human proofing for an input such as a number
            asc_or_desc = str.lower(asc_or_desc)
            if asc_or_desc == "a": 
                #if input is a
                x = "SELECT * FROM product\nORDER BY price ASC" 
                # becomes sql statement ascending 
            elif asc_or_desc == "d": 
                    #if input is d
                x = "SELECT * FROM product\nORDER BY price DESC" 
                #becomes sql statement descending
        except: 
            print("Invalid Input, try typing just the letter\n") #if answer is not a or d 
        sql = x
            #SQL statement for showing everything in products
        cursor.execute(sql)
            #executes the statement
        results = cursor.fetchall()
            #fetches all data that has been received and turns it into an variable
        print(f"|{'product_id':<11}|{'name':<29}|{'age_rating':<11}|{'price':<7}|{'description':<69}|{'genre':<29}|{'gamerating':<9}|\n")
            #structures the data with column names
        for item in results:
            print(f"|{item[0]:<11}|{item[1]:<29}|{item[2]:<11}|{item[3]:<7}|{item[4]:<69}|{item[5]:<29}|{item[6]:<9}|\n")
                #prints the data below it
    except:
        print("These products table could not be shown\n") 
        #could not be shown

def show_product_general(connection): #function when price is irrelevant 
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM product"
            #SQL statement for showing everything in products
        cursor.execute(sql)
            #executes the statement
        results = cursor.fetchall()
            #fetches all data that has been received and turns it into an variable
        print(f"|{'product_id':<11}|{'name':<29}|{'age_rating':<11}|{'price':<7}|{'description':<69}|{'genre':<29}|{'gamerating':<9}|\n")
            #structures the data with column names
        for item in results:
            print(f"|{item[0]:<11}|{item[1]:<29}|{item[2]:<11}|{item[3]:<7}|{item[4]:<69}|{item[5]:<29}|{item[6]:<9}|\n")
                #prints the data below it
    except:
        print("These products table could not be shown\n") 
        #could not be shown

def show_user(connection):
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM user"
            #SQL statement for showing everything in products
        cursor.execute(sql)
            #executes the statement
        results = cursor.fetchall()
            #fetches all data that has been received and turns it into an variable
        print(f"|{'user_id':<7}|{'first_name':<14}|{'surname':<14}|{'phone_number':<14}|{'email':<59}|\n")
            #structures the data with column names
        for item in results:
            print(f"|{item[0]:<7}|{item[1]:<14}|{item[2]:<14}|{item[3]:<14}|{item[4]:<59}|\n")
                #prints the data below it
    except:
        print("The user table could not be shown\n")



def show_sales(connection):
    try:
        cursor = connection.cursor()
        sql = "SELECT sales_id, sales.user_id, sales.product_id, name, price, sale_date FROM sales\nJOIN product ON product.product_id = sales.product_id\nJOIN user ON user.user_id = sales.user_id\nORDER BY sales_id"
            #Statement to get everything from the sales table and compile it here
        cursor.execute(sql)
            #executes the statement
        results = cursor.fetchall()
            #fetches all data that has been received and turns it into an variable
        print(f"|{'sales_id':<14}|{'user_id':<14}|{'product_id':14}|{'name':<29}|{'price':<7}|{'sales_date':<29}|\n")
            #structures the data with column names
        for item in results:
            print(f"|{item[0]:<14}|{item[1]:<14}|{item[2]:<14}|{item[3]:<29}|{item[4]:<7}|{item[5]:<29}|\n")
                #prints the data below it
    except:
        print("The sales table could not be shown\n")



#ADD FUNCTIONS



def add_product(connection, product_name, product_age_rating, product_price, product_description, product_genre, product_game_rating):
    try:
        #Required variables
        cursor = connection.cursor()
            #connection into sql
        sql = "INSERT INTO product(name, age_rating, price, description, genre, game_rating) VALUES (?,?,?,?,?,?)"
            #statement for receiving multiple values from user input
        cursor.execute(sql,(product_name, product_age_rating, product_price, product_description, product_genre, product_game_rating))
            #executes using the data received from the actual python program and uses it in the sql statement 
        connection.commit()
            #commits data and adds it to sql  file
        print("Successfully added")
    except:
        print("This item could not be added. Potential Duplicate or invalid inputs. Please try again\n")



def add_user(connection, user_first_name, user_surname, user_phone_number, user_email):
    try:
        #Required variables
        cursor = connection.cursor()
            #connection into sql
        sql = "INSERT INTO user(first_name, surname, phone_number, email) VALUES (?,?,?,?)"
            #statement for receiving multiple values from user input
        cursor.execute(sql,(user_first_name, user_surname, user_phone_number, user_email))
            #executes using the data received from the actual python program and uses it in the sql statement 
        connection.commit()
        print("Successfully added")
            #commits data and adds it to sql  file
    except:
        print("This item could not be added. Potential duplicate or invalid inputs. Please try again\n")



#DELETE ITEMS 



def delete_item(connection, table, delete_an_item_id, sql):
    try:
        cursor = connection.cursor()
            #sql statement that removes an entire item and its contents from the sql database
        cursor.execute(sql,(delete_an_item_id,))
        num_rows_affected = cursor.rowcount 
            #checks if any rows were affetced
        if num_rows_affected == 0: 
            #if none were this means that the item does not exist
            print("Can't find item as it does not exist\n")
        else:
            connection.commit()
            print("Successfully deleted\n")
                #commits the deleted change
    except:
        print("Item doesn't exist and cannot be deleted. Please refer to the table above to select a correct variable\n")
        #if the sql statement cannot be executed it means something has gone wrong within SQL




#UPDATE ITEMS



def update(connection, table_update):
    try:
        cursor = connection.cursor()
        if table_update == "p":
                #represents products
            show_product_general(connection)
            update_specific = input("What in products would you like to update? \n\nPlease type one the following by refering to the table shown above:\nproduct_id\nname \nage_rating \nprice \ndescription\ngenre\ngame_rating\n\n\n")
                #Asks for one of the column names
            try:    
                update_specific = str.lower(update_specific)
                z = f"UPDATE product SET {update_specific} =? WHERE product_id = ?"
                    #updates the specific item that has been entered in SQL. The try means that of it does not work the program will not stop
            except:
                print("Invalid input, try checking the spelling")
                    #recommends a fix
        if table_update == "u":
            show_user(connection)
                #represents users
            update_specific = input("What in users would you like to update? \n\nPlease type one of the following refering to the table shown above:\nuser_id\nfirst_name \nsurname \nphone_number \nemail\n\n\n")
                #asks for user specific columns
            try:
                update_specific = str.lower(update_specific)
                z = f"UPDATE user SET {update_specific} =? WHERE user_id = ?"
                    #sets the update specific variable into the string
            except:
                print("Invalid input, try checking the spelling")
        id = input("What is the ID of the item you want to change? (eg. 5)\n")
            #Asks for the id
        change = input(f"What would you like to change the {update_specific} to? \n")
            # asks for the change to be made and shows with the F string what the user has selected to be changed
        sql = z
            #sql statement for changiing a specific input from the user
        cursor.execute(sql, (change,id))
            #executes the change using id and change
        num_rows_affected = cursor.rowcount
        if num_rows_affected == 0: 
            #checks if the item exists
            print("Can't find item\n")
        else:
            connection.commit()
            print("Successfully updated")
            #commits the change from a user input
    except:
        print("Item doesn't exist and cannot be updated\n")
            #if it doesn't work it means the user has inputed a valid table variable



#SHOW ITEMS



def options_show(connection): 
    #Function for the options of showing 
    options_show = input("What would you like to see?\np for product \ns for sales, \nu for user \n")
    #Asks what the user would like to view
    try:
        options_show == str.lower(options_show)
        if options_show == "s":
            show_sales(connection)
                #returns back the table for sales
        elif options_show == "u":
            show_user(connection)
                #returns back the table for user
        elif options_show == "p":
            show_product(connection)
                #returns back the table for products 
    except:
        print("Not a valid input, try typing just the letter")





