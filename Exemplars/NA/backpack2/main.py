import sqlite3

def show_product():#brings the data base
  db = sqlite3.connect('backpack.db') 
  cursor = db.cursor()
  sql = "SELECT * FROM item;"
  cursor.execute(sql)
  #db.commit() #only commit if you insert/delete etc.
  results = cursor.fetchall()
  for item in results:
    print(f"{item[0]:<8}{item[1]:<10}{item[2]:<50}")
  db.close()
  
def show_customer_item(): #to link with sqlit and python made a function
  db = sqlite3.connect('backpack.db') 
  cursor = db.cursor()
  sql = "SELECT * FROM customer;"
  cursor.execute(sql)
  results = cursor.fetchall()
  for item in results:
    print(f"{item[0]:<8}{item[1]:<10}{item[2]:<50}")
  db.close()

def loooop(stopping,customer_sales):#sales
  if stopping == "y":
    return  
  elif stopping == "n":
    customer_sales = int(input("what item do u want? (ID) \n= "))#ask the user what item they want
    stopping = input("is that all?  y - n \n= ")
  if stopping == "y":
    return
  else:
   print("...")
  loooop(stopping,customer_sales)
    
#this is the menu...
while True:
  user = int(input("1. show product \n2. customer list \n= "))
  if user == 1:
    show_product()
    customer_sales = int(input("what item do u wan? (ID) \n= "))
    stopping = input("is that all?  y - n \n= ")

    loooop(stopping,customer_sales)

  elif user == 2:
    show_customer_item()
    break
  else:
    print("...")
'''
def delete_item(connection, item_name):
 cursor = connection
'''
def information_customers():#function to get info from customers
  user = input("What is your account number?")#ask users their account number
  flag = True
  while flag:
   if len(user) == 16:#the digit need to be 16
     flag = False
   else:
     print("it need to be 16 digit")
     user = input("What is your account number?")
   
  user1 = input("what is your phone number")
  flag = True 
  while flag:
    if len(user1) == 10:#10 digit number need
      user2 = input("What is your address?")
      flag = False
    else:
      print("it need to be 10 digit")
      user1 = input("what is your phone number")
  user3 = input("what is your name?")
  
  return (user),(user1),(user2),(user3)
    
  
information_customers()




