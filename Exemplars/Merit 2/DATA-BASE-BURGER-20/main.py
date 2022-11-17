from functions import show_burger_info,add_item,delete_item,update_item,order_item

import sqlite3
DATABASE_FILE = "burgerdatabase (1).db"  

#'''        
while True:    # infinte loop
  try:   #error checker
    answer_id = int(input("Are you are customer or a staff member? \n 1-customer , 2-staff member \n enter here: "))  
    # staff or custermer
    print()
    if answer_id == 1:   #custermer
      with sqlite3.connect(DATABASE_FILE) as connection:
        print("Here is our menu!")
        print()
        show_burger_info() # show menu
        order_item() # order items

      
    elif answer_id == 2:#staff member
      while True:  # infinte loop
        password = input("What is the password? (it's defenitly not fish) or ENTER '1' to leave\n enter password here: ")  #password not fish
        print()
        if password == "fish":
          print("ACCESS GRANTED")  #granted
          print()
          wot_to_do = input("What would you like to do? 1)Options OR 2)Leave \nEnter Here: ")  # leave or view options
          while True:
            if wot_to_do == "1": # look at options(delete,add,change database)
              print()
              options = input("what would you like to do:\n\n1)update items\n2)delete items\n3)add items\n4)view tables\n5)leave\nEnter here: ") # what options
              print()
              if options == "1":  #go update items
                with sqlite3.connect(DATABASE_FILE) as connection:
                  print()
                  update_item(connection)  # update the items
              elif options == "2":  #delte items
                with sqlite3.connect(DATABASE_FILE) as connection:
                  print()
                  delete_item(connection)         # deleting functions         
              elif options == "3":  #add items
                with sqlite3.connect(DATABASE_FILE) as connection:
                  print()
                  add_item(connection)    # adding items
              elif options == "4":  # view tables
                 with sqlite3.connect(DATABASE_FILE) as connection:
                  show_burger_info()
                  print()
              elif options == "5":   #bye
                print("bye")
                print()
                break
              else:
                print("INVALID ANSWER")
              
            elif wot_to_do == "2":   #leave
              print()
              break
            else:
              print("INVALID ANSWER")  #invalid answer
              break
        else:
          again = input("try again = yes , leave = no , type: yes or no\n ENTER HERE:")
          print()  # try again for password
          if again == "no":
            break
          elif again != "yes":
            print("invalid answer")
            print()
            break
        
    else:
      print("Your answer was not an option please try again!")
  except:
    print("INVALID ANSWER or THERE WAS A PROBLEM WITH THE CODE PLEASE TRY AGAIN !!!")
    print()

#'''





#if __name__ == "__main__":  # TESTING PART ( NOT PART OF CODE )
  #update_item()
  #add_item()
  #delete_item()
  #show_burger_info()
  #order_item()
