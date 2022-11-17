import sqlite3, time
from replit import clear

con = sqlite3.connect("pizzaexportedtest.db")
c = con.cursor()

def interface():
  c.execute("BEGIN")
  
  while True:
    try:
      print("1 = insertinto\n2 = createtable\n3 = selectfrom\n4 = makequery\n5 = jointable\n6 = commit\n7 = don't commit / end program")
      execution = int(input("\nwhatchu wanna do: "))
      clear()
      if execution == 1:
        c.execute(insert_into())
        time.sleep(1)
        clear()
      if execution == 2:
        c.execute(create_table())
        time.sleep(1)
        clear()
      if execution == 3:
        c.execute(select_from())
        time.sleep(1)
        clear()
      if execution == 4:
        c.execute(make_query())
        time.sleep(1)
        clear()
      if execution == 5:
        c.execute(join_table())
        time.sleep(1)
        clear()
      if execution == 6:
        con.commit()
        return "Committed"
      if execution == 7:
        return "Not Committed"
        
      elif execution > 7 or execution < 1:
        print("hey!!! don't do that\n")
      execution = 0
      
    except ValueError:
      print("integer please")
      time.sleep(1)
      clear()

      
def insert_into():
  """inserts data into existant table. use create_table() first."""
  
  data = []
  
  table = input("what table do you want to insert into: ")
  data_num = int(input("how many columns are there in this table: "))
  for i in range(data_num):
    value = input("value = ")
    
    if value.isdigit() == False:
      value = f"'{value}'"
    else:
      value = int(value)

    data.append(value)
    value = 0

  data = list(map(str, data))
  data_sep = (', '.join(data))
  
  return f"INSERT INTO {table} VALUES ({data_sep})"


def create_table():
  """creates table if it doesn't already exist"""
  while True:
    while True:
      
      table_name = input("what is the name of the table: ")
     
      column1 = input("name of first column: ")
      column1_type = input("what type of column is it: ")
      
      column2 = input("name of second column: ")
      column2_type = input("what type of column is it: ")
      
      column3 = input("name of third column: ")
      column3_type = input("what type of column is it: ")
    
      if column1 == column2 or column1 == column3 or column1 == column3:
        print("Error: duplicate column name.")
        time.sleep(2)
        clear()
        break

      else:
        return f"CREATE TABLE IF NOT EXISTS {table_name} ({column1} {column1_type}, {column2} {column2_type}, {column3} {column3_type})"


def select_from():
  """selects data from a table"""
  data = []
  
  table = input("what table do you want to select from: ")
  data_num = int(input("how many values do you want to select: "))
  for i in range(data_num):
    value = input(f"what value do you want to select from {table}: ") #leave blank and it will select all from a table

    if value == "":
      value = "*"
      data.append(value)
      break
    
    data.append(value)
    value = 0

  data = list(map(str, data))
  data_sep = (', '.join(data))
  
  return f"SELECT {data_sep} FROM {table}"


def make_query():
  """makes query"""
  query = input("write the whole query here: ")
  return query


def join_table():
  """only joins two tables, but you can select multiple things"""
  data = []
  
  tables = input("tables you want to select from (sep by comma): ")
  data_num = int(input("how many values do you want to select: "))
  for i in range(data_num):
    value = input(f"what value do you want to select from {tables}: ") #leave blank and it will select all from a table

    if value == "":
      value = "*"
      data.append(value)
      break
    
    data.append(value)
    value = 0

  jointable = input("what table do you want to join from: ")
  joinvalue1 = input("")
  
  jointable_onto = input("what table do you want to join onto: ")
  joinvalue2 = input("")
  
  data = list(map(str, data))
  data_sep = (', '.join(data))
  
  return f"""SELECT {data_sep} FROM {tables} JOIN {jointable} ON {jointable}.{joinvalue1} = {jointable_onto}.{joinvalue2};"""

# print(interface())