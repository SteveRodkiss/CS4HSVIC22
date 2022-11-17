import sqlite3

DATABASE_FILE = "burgerdatabase (1).db"

def order_item():  # function for ordering
  while True:    
    try:
      tot_burger_price = []
      burger_patties= []     # STORE all the prices,patties,sauces,topping
      burger_sauces = []   
      burger_toppings = []
  
    
      num_burger = int(input("How many burger would you like to order?\n(MAX 5)\nENTER HERE:"))   # amount of burger they want and also use that var as the amount the for loop is repeated          
      print()
      if num_burger > 0 and num_burger <= 5:  #limiting to 1-5
        num_burg = 0
        for num_burger in range(num_burger):  #looping depending on amount of burgers
          num_burg += 1
          print(f"BURGER {num_burg}")
          connection = sqlite3.connect(DATABASE_FILE)
          cursor = connection.cursor()
                        #patties order
          sql = "SELECT name,price,rating FROM patties"
          item_to_find = input("What pattie would you like to order? ")
          cursor = connection.cursor()
          cursor.execute(sql)
          burger_info = cursor.fetchall()  
          for item in burger_info:
            if item_to_find == str(item[0]):  #checking if item to find is on the menu
              print(f"\n{'Name':<20}{'Price':<20}{'Rating':<20}")    
              print(f"{item[0]:<20}{item[1]:<20}{item[2]:<20}")
              print()  #if so print it out
              burger_patties.append(item[0])  # add to patties list
              tot_burger_price.append(item[1]) #add price to tot price
                        # topping order
          sql = "SELECT name,price,rating FROM topping"
          item_to_find = input("What topping would you like to order? ")
          cursor = connection.cursor()
          cursor.execute(sql)          #same as before
          burger_info = cursor.fetchall()  
          for item in burger_info:
            if item_to_find == str(item[0]):
              print(f"\n{'Name':<20}{'Price':<20}{'Rating':<20}")    
              print(f"{item[0]:<20}{item[1]:<20}{item[2]:<20}")
              print()
              burger_toppings.append(item[0])
              tot_burger_price.append(item[1])
                        #sauce order
  
          sql = "SELECT name,price,rating FROM sauce"
          item_to_find = input("What sauce would you like to order? ")
          cursor = connection.cursor()
          cursor.execute(sql)
          burger_info = cursor.fetchall()    #same as before
          for item in burger_info:
            if item_to_find == str(item[0]):
              print(f"\n{'Name':<20}{'Price':<20}{'Rating':<20}")    
              print(f"{item[0]:<20}{item[1]:<20}{item[2]:<20}")
              print()
              burger_sauces.append(item[0])
              tot_burger_price.append(item[1])
        print()
        print("CHECKOUT TIME")
        print()
        num_burg2 = 0
        for num_burger in range(num_burger +1):  # looping for the amount of burgers they ordered
          print(f"BURGER {num_burg2 + 1}") # prints the fisrt burger and what you ordered and also burger2 ......
          print(f"Pattie:{burger_patties[num_burg2]}\nTopping:{burger_toppings[num_burg2]}\nSauce:{burger_sauces[num_burg2]}") #prints the patties,toppings and sauce for each burger
          num_burg2 += 1
          print()
        print(f"The Total price is: ${sum(tot_burger_price)}\nTHANKS") # sum of the total prices
        break
      else:
        print("INVALID ANSWER")
    except:
      print("SOMETHING WENT WRONG or INVALID CHOICE\n Try again")
      print()
  




def show_burger_info(): 
  while True:
    try:
      with sqlite3.connect(DATABASE_FILE) as connection:
        '''nicely print burger info'''
        option_pts  = input("What would you like to see\n1)patties\n2)toppings\n3)sauce\nEnter here:")  # choose what to view
        print()
        #depending on which option_pts you choose it will print a different sql
        if option_pts == "1":
          sql = "SELECT * FROM patties" #show all patties
        elif option_pts == "2":
          sql = "SELECT * FROM topping"#show all toppings
        elif option_pts == "3":
          sql = "SELECT * FROM sauce"#show all sauces
        else:
          print("INVALID ANSWER")
          break
          print()
        cursor = connection.cursor()
        cursor.execute(sql)
        burger_info = cursor.fetchall()
        print(f"\n{'Name':<20}{'Price':<20}{'Rating':<20}")
        

        for item in burger_info:
          print(f"{item[1]:<20}{item[2]:<20}{item[3]:<20}") #for each item there is print its name,price,rating 
        leave_qestion = int(input("Continue viewing(1) or finished viewing(2)\nEnter Here:")) #leave or continue
        print()
        
    
        
        if leave_qestion == 1:
          print("Okay continue")
          print()
        elif leave_qestion == 2:
          print("Okay")
          print()
          break
        else:
          print("INVALID ANSWER")
    except:
      print("something went wrong")
  
    connection.close()





#ADD
def add_item(connection):
  try:
    '''add item to backpack database'''
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()   # name,price,rating for new item
    item_name = input("What would you like the name for your item to be.\nEnter Here:")
    print()#new item name
    item_price = int(input("What would you like the price for your item to be.\nEnter Here:"))
    print() #new item price
    item_rating = int(input("What would you like the rating(0-10) for your item to be.\nEnter Here:")) #new item rating
    print()
    item_table = int(input("Where would you like this item to go?\n1)patties\n2)toppings\n3)sauce\nENTER HERE:")) #Which table it goes into
    if item_table == 2:   # topping table
      sql = "INSERT INTO topping (name,price,rating) Values(?,?,?)"
      cursor.execute(sql,(item_name,item_price,item_rating))
      print("your items have been added to the menu")
      print()
      connection.commit()
    elif item_table == 1:   #pattie table
      sql = "INSERT INTO patties (name,price,rating) Values(?,?,?)"
      cursor.execute(sql,(item_name,item_price,item_rating))
      print("your items have been added to the menu")
      print()
      connection.commit()
    elif item_table == 3:  #sauce table
      sql = "INSERT INTO sauce (name,price,rating) Values(?,?,?)"
      cursor.execute(sql,(item_name,item_price,item_rating))
      print("your items have been added to the menu")
      print()
      connection.commit()
    else:
      print("ANSWER DID NOT FIT CRITERIA")
  except:
    print("INVALID ANSWER")
    print()





    
 #DELETE
def delete_item(connection):
  '''delet item by name'''
  try:
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    delete_name = input("What would you like to delete (name)\nEnter here:")
    print()#what is the name for the item you want to delete
    item_table = int(input("In which table would you like to delete it from?\n1)patties\n2)toppings\n3)sauce\nENTER HERE:")) #and what table is it from
    if item_table == 2:   # topping table
      sql = "DELETE FROM topping WHERE name = ?"
      cursor.execute(sql,(delete_name,))
      print("your item has been deleted from the menu")
      print()
      connection.commit()
    elif item_table == 1:   #pattie table
      sql = "DELETE FROM patties WHERE name = ?"
      cursor.execute(sql,(delete_name,))
      print("your item has been deleted from the menu")
      print()
      connection.commit()
    elif item_table == 3:  #sauce table
      sql = "DELETE FROM sauce WHERE name = ?"
      cursor.execute(sql,(delete_name,))
      print("your item has been deleted from the menu")
      print()
      connection.commit()
       # delete 
    else:
      print("ANSWER DID NOT FIT CRITERIA")
    num_rows_affected = cursor.rowcount
    if num_rows_affected == 0 :
      print("cant find item")
    else:
      connection.commit()
  except:
    print("item no exist")






#UPDATE
def update_item(connection):
  try:
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    item_name = input("What is the name of the item you want to update?\nEnter here:")
    print()#what is the selected item you want to updates name
    update_price = input("What would you like the updated price to be?\nEnter Here:")
    print() #what will be its new price
    item_table = int(input("In which table would you like to update it from?\n1)patties\n2)toppings\n3)sauce\nENTER HERE:"))
    print()#in which table does it belong in
    if item_table == 2:   # topping table
      sql = "UPDATE topping SET price = ?,WHERE name = ?"
      cursor.execute(sql,(update_price,item_name))
      print("your item has been updated to the menu")
      print()
      connection.commit()
    elif item_table == 1:   #pattie table
      sql = "UPDATE patties SET price = ? WHERE name = ?"
      cursor.execute(sql,(update_price,item_name))
      print("your item has been updated to the menu")
      print()
      connection.commit()
    elif item_table == 3:  #sauce table
      sql = "UPDATE sauce SET price = ?,WHERE name = ?"
      cursor.execute(sql,(update_price,item_name))
      print("your item has been updated to the menu")
      print()
      connection.commit()

    else:
      print("ANSWER DID NOT FIT CRITERIA")
    num_rows_affected = cursor.rowcount
    if num_rows_affected == 0:
      print("cant update item")
  
    else:
      connection.commit()
  
    
  except:
    print("failed to update")
