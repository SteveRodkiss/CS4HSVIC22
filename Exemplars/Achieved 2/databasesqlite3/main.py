import sqlite3, time, os
from replit import clear

con = sqlite3.connect("pizzaexportedtest.db")
c = con.cursor()


def pizza_interface():
  """list orders, list names, time"""
  
  if os.path.exists("pizzaexportedtest.db-journal"): # delete non commited stuff if already exists
    os.remove("pizzaexportedtest.db-journal")
  
  c.execute("BEGIN") # turns off auto commit
  
  while True:
    try:
      print("What would you like to do?\n\n1. Make an order\n2. List all pizzas\n3. List all orders\n4. Quit program, commit order(s)\n5. Quit program, DON'T commit order(s)\n\n(DO NOT COMMIT IF YOUR ORDER WAS WRONG OR YOU DIDN'T ORDER)") # although, it would do nothing if you commited with no order
      user_input = int(input("\nInput your option as the number: "))
      clear() # clears console
      
      if user_input == 1:
        make_orders()
      if user_input == 2:
        print(list_pizzas())
        thing = input("press enter to go back                                    ") # using an input holds the user in place to view the pizzas until they press enter
        clear() 
      if user_input == 3:
        print(list_orders())
        thing = input("press enter to go back                                    ") # same thing here
        clear()
      if user_input == 4: # commit
        if os.path.exists("pizzaexportedtest.db-journal"):
          con.commit()
          os.remove("pizzaexportedtest.db-journal")
          return "Committed. Bye bye!!!"
        print("there's nothing to commit!")
      if user_input == 5: # dont commit, delete failed orders
        if os.path.exists("pizzaexportedtest.db-journal"): # same thing here
          os.remove("pizzaexportedtest.db-journal")
          return "Order cancelled, NOT COMMITTED. Later alligator!!!!!"
        return "NOT Committed. Cya!!!"
      if user_input > 5 or user_input < 1:
        print("That is not an option\n")

      time.sleep(1)
      clear()
      
    except ValueError:
      print("\nexpected integer value :nerd:\n")


def make_orders():
  """get date, name, pizza, pizza size"""
  while True:
    while True:
      try:
        date = input("What day do you want to pick up? (example format: 2022/07/11) ")
        
        if date.isalnum() == True: # catches SOME false formats. I couldn't figure out how to only get the format YYYY/MM/DD
          print("wrong format stoopid XD")
          time.sleep(2)
          clear()
          break
        
        name = input("what is your first name? ")
        
        if name.isdigit() == True: # catches all false formats
          print("wrong format stoopid XD")
          time.sleep(2)
          clear()
          break
        
        clear()
        print(list_pizzas())
        pizza = int(input("What pizza do you want? (format: use the ids, not the name) ")) # the "except ValueError" catches this
        
        if pizza < 1 or pizza > 5:
          print("wrong format stoopid XD")
          time.sleep(2)
          clear()
          break
        
        clear()
        print("Small, Medium, Large, XL")
        pizza_size = input("What size do you want your pizza? (use name of size) ")
        
        if pizza_size != "Small" and pizza_size != "Medium" and pizza_size != "Large" and pizza_size != "XL": # manual catching muahahaha
          print("wrong format stoopid XD")
          time.sleep(2)
          clear()
          break
        
        clear()
        
        tuple_to_orders = (date,name)
        tuple_to_porders = (pizza,pizza_size)
        
        sql = "INSERT INTO orders (order_time,order_fname) VALUES (?,?)"
        sql2 = "INSERT INTO pizza_orders (pizza_id,pizza_size) VALUES (?,?)"
      
        c.execute(sql, tuple_to_orders)
        c.execute(sql2, tuple_to_porders)
      
        return "Order made!!!"
      except ValueError:
        print("that is NOT the right format...")
        time.sleep(2)
        clear()
  # insert into pizza orders, orders using tuple, ignore id cuz of primary key, fix autoincrement


def list_pizzas():
  # MR RODKISS WROTE THIS
  query = "SELECT * FROM pizza"
  c.execute(query)
  rows = c.fetchall()
  print("ID, NAME, TOPPINGS, PRICE")
  for row in rows:
    print(row)
  return ""


def list_orders():
  # MR RODKISS WROTE THIS (from tutorial)
  query = "SELECT * FROM orders"
  c.execute(query)
  rows = c.fetchall()
  print("ID, DATE, NAME")
  for row in rows:
    print(row)
  return ""


print(pizza_interface())

con.close()