import sqlite3

DATABASE_FILE = "basketball.db"
#functions
'''Functions'''
def show_basketball(connection,table_name,column_1, column_2):
    '''nicely print the basketball information'''
    cursor = connection.cursor()
    #selecting two coloumns from table 
    sql = f"SELECT {column_1}, {column_2} FROM {table_name}"
    cursor.execute(sql)
    results = cursor.fetchall()
    #print statement
    print(f"\n{column_1:<12}{column_2 :<15}")
    for player in results:
        print(f"{player[0]:<10}{player[1]:<15}")

#function for adding player
def add_player(connection, first_name, last_name):
    '''add player to basketball database'''
    cursor = connection.cursor()
    #sql query 
    sql = "INSERT INTO player(first_name, last_name) VALUES (?,?)"
    cursor.execute(sql,(first_name, last_name))
    connection.commit()

def show_basketball2(connection):
    '''nicely print the mvp information'''
    cursor = connection.cursor()
    #sql query
    sql = f"""SELECT mvp.year, player.first_name, player.last_name FROM mvp
JOIN player on player.player_id = mvp.player_id"""
    cursor.execute(sql)
    results = cursor.fetchall()
    #print statement
    print(f"\n{'year':<12}{'first name' :<15}{'last name' :<15}")
    for player in results:
        print(f"{player[0]:<10}{player[1]:<15}{player[2]:<15}")

def show_basketball3(connection):
    '''nicely print which team a player plays for'''
    cursor = connection.cursor()
    #sql query
    sql = f"""SELECT player.first_name, player.last_name, team.team_name FROM team_player
JOIN player on player.player_id = team_player.player_id
JOIN team on team.team_id = team_player.team_id"""
    cursor.execute(sql)
    results = cursor.fetchall()
    #print statement
    print(f"\n{'First Name':<12}{'Last Name' :<15}{'Team Name' :<15}")
    for player in results:
        print(f"{player[0]:<10}{player[1]:<15}{player[2]:<15}")

while True:
    try:
        
        #taking input from user
        user_input = input('''\nWhat do you want to see? 
    type the number in the bracket then click enter to select each option. 
    Click(1) to view tables ''')
        if user_input == '1':
            #after user inputs '1' asking which data the user wants to view
            data_selection = input('''\nWhich data do you want to view?
    Click(1) to show the player data
    Click(2) to show the team data
    Click(3) to show mvp data
    Click(4) to show players and their respective teams
    Click(5) to STOP ''')
    #printing data according to which data the user wants to see
            if data_selection == '1':
                with sqlite3.connect('./basketball.db') as connection:
                    show_basketball(connection,'player', 'first_name', 'last_name')
                    
            elif data_selection == '2':
                with sqlite3.connect('./basketball.db') as connection:
                    show_basketball(connection,'team','conference', 'team_name')
                    
            elif data_selection == '3':
                with sqlite3.connect('./basketball.db') as connection:
                    show_basketball2(connection)
                    
            elif data_selection == '4':
                with sqlite3.connect('./basketball.db') as connection:
                    show_basketball3(connection)
                
            elif data_selection == '5':
                with sqlite3.connect('./basketball.db') as connection:
                    show_basketball3(connection)
                    break
                    
                    
            else:
                print('That is not an option. Please try again.')
    #if user does not click the available options it will print the following 
        else: 
            print('That is not an option')
    except:
        print('Not an avaliable option')








