import sqlite3
import traceback

'''this is an interactive game database program, made by Ethan Davidson :)'''


TARGET_DATABASE_FILE = "game_database.db"

'''my functions'''


def unformatted_show_games(connection):
    '''just an example function to showcase how bad the table looks without any formatting'''

    cursor = connection.cursor()
    query = "SELECT * FROM Games"
    cursor.execute(query)
    results = cursor.fetchall()
    print(results)


def show_games(connection):
    '''prints out the games table in a nice format'''

    try:
        cursor = connection.cursor()
        query = "SELECT Games.Name, Games.Rating, Genres.Genre, Prices.Price, Sizes.Size FROM Games JOIN Genres ON Games.Genre_ID=Genres.ID JOIN Prices ON Games.Price_ID=Prices.ID JOIN Sizes ON Games.Size_ID=Sizes.ID;"
        cursor.execute(query)
        results = cursor.fetchall()
        print(
            f"\n{'Name':<20}{'Rating [/10]':<20}{'Genre':<20}{'Price':<20}{'Size':<20}")
        for info in results:
            print(
                f"{info[0]:<20}{info[1]:<20}{info[2]:<20}{info[3]:<20}{info[4]:<20}")
    except Exception as error:
        traceback.print_exc()
        print("\nUh oh, something went wrong while trying to SHOW_GAMES")


def list_games(connection):
    '''lists all games present in the Games Table'''

    try:
        cursor = connection.cursor()
        query = "SELECT Name FROM Games;"
        cursor.execute(query)
        results = cursor.fetchall()
        for info in results:
            print(f"{info[0]:<20}")
    except Exception as error:
        traceback.print_exc()
        print("\nUh oh, something went wrong while trying to LIST_GAMES")


def add_game(connection, game_name, game_rating, game_size_ID, game_price_ID, game_genre_ID):
    '''allows the user to pretty safely add games to the table'''

    try:
        cursor = connection.cursor()
        query = "INSERT INTO Games(Name, Rating, Size_ID, Price_ID, Genre_ID) VALUES (?,?,?,?,?)"
        cursor.execute(query, (game_name, game_rating,
                       game_size_ID, game_price_ID, game_genre_ID))
        connection.commit()
        print("\nGame was added successfully!\n")
    except Exception as error:
        traceback.print_exc()
        print("\nUh oh, couldn't ADD_GAME, something went wrong!")


def delete_game(connection, game_name):
    '''allows the user to fairly safely remove games from the table'''

    try:
        cursor = connection.cursor()
        query = "DELETE FROM Games WHERE Name = ?"
        cursor.execute(query, (game_name,))
        num_rows_affected = cursor.rowcount
        if num_rows_affected == 0:
            print("\nCould not find and DELETE_GAME (likely chosen game does not exist)!")
        else:
            connection.commit()
            print("\nChosen game was deleted successfully!\n")
    except Exception as error:
        traceback.print_exc()
        print("Uh oh, something went wrong while trying to DELETE_GAMES (likely chosen game does not exist)")


def update_game_rating(connection, game_name, new_rating):
    '''allows the user to quite safely update game rating'''

    try:
        cursor = connection.cursor()
        query = "UPDATE Games SET Rating = ? WHERE Name = ?"
        cursor.execute(query, (new_rating, game_name))
        num_rows_affected = cursor.rowcount
        if num_rows_affected == 0:
            print(
                "\nCould not find and UPDATE_GAME_RATING (likely chosen game does not exist)")
        else:
            connection.commit()
            print("\nGame rating was changed successfully!\n")
    except Exception as error:
        traceback.print_exc()
        print("Uh oh, something went wrong while trying to UPDATE_GAME_RATING (likely chosen game does not exist)")


def order_games_by_price(connection):
    '''function which orders games by price'''

    try:
        cursor = connection.cursor()
        query = "SELECT Games.Name, Games.Rating, Genres.Genre, Prices.Price, Sizes.Size FROM Games JOIN Genres ON Games.Genre_ID=Genres.ID JOIN Prices ON Games.Price_ID=Prices.ID JOIN Sizes ON Games.Size_ID=Sizes.ID ORDER BY Price_ID;"
        cursor.execute(query)
        results = cursor.fetchall()
        print(
            f"\n{'Name':<20}{'Rating [/10]':<20}{'Genre':<20}{'Price':<20}{'Size':<20}")
        for info in results:
            print(
                f"{info[0]:<20}{info[1]:<20}{info[2]:<20}{info[3]:<20}{info[4]:<20}")
    except Exception as error:
        traceback.print_exc()
        print("\nUh oh, something went wrong while trying to ORDER_BY_PRICE")


def order_games_by_size(connection):
    '''function which orders games by size'''

    try:
        cursor = connection.cursor()
        query = "SELECT Games.Name, Games.Rating, Genres.Genre, Prices.Price, Sizes.Size FROM Games JOIN Genres ON Games.Genre_ID=Genres.ID JOIN Prices ON Games.Price_ID=Prices.ID JOIN Sizes ON Games.Size_ID=Sizes.ID ORDER BY Size_ID;"
        cursor.execute(query)
        results = cursor.fetchall()
        print(
            f"\n{'Name':<20}{'Rating [/10]':<20}{'Genre':<20}{'Price':<20}{'Size':<20}")
        for info in results:
            print(
                f"{info[0]:<20}{info[1]:<20}{info[2]:<20}{info[3]:<20}{info[4]:<20}")
    except Exception as error:
        traceback.print_exc()
        print("\nUh oh, something went wrong while trying to ORDER_BY_SIZE")


def order_games_by_rating(connection):
    '''function which orders games by rating'''

    try:
        cursor = connection.cursor()
        query = "SELECT Games.Name, Games.Rating, Genres.Genre, Prices.Price, Sizes.Size FROM Games JOIN Genres ON Games.Genre_ID=Genres.ID JOIN Prices ON Games.Price_ID=Prices.ID JOIN Sizes ON Games.Size_ID=Sizes.ID ORDER BY Rating;"
        cursor.execute(query)
        results = cursor.fetchall()
        print(
            f"\n{'Name':<20}{'Rating [/10]':<20}{'Genre':<20}{'Price':<20}{'Size':<20}")
        for info in results:
            print(
                f"{info[0]:<20}{info[1]:<20}{info[2]:<20}{info[3]:<20}{info[4]:<20}")
    except Exception as error:
        traceback.print_exc()
        print("\nUh oh, something went wrong while trying to ORDER_BY_RATING")


def order_games_by_genre(connection):
    '''function which orders games by genre'''

    try:
        cursor = connection.cursor()
        query = "SELECT Games.Name, Games.Rating, Genres.Genre, Prices.Price, Sizes.Size FROM Games JOIN Genres ON Games.Genre_ID=Genres.ID JOIN Prices ON Games.Price_ID=Prices.ID JOIN Sizes ON Games.Size_ID=Sizes.ID ORDER BY Genre_ID;"
        cursor.execute(query)
        results = cursor.fetchall()
        print(
            f"\n{'Name':<20}{'Rating [/10]':<20}{'Genre':<20}{'Price':<20}{'Size':<20}")
        for info in results:
            print(
                f"{info[0]:<20}{info[1]:<20}{info[2]:<20}{info[3]:<20}{info[4]:<20}")
    except Exception as error:
        traceback.print_exc()
        print("\nUh oh, something went wrong while trying to ORDER_BY_GENRE")


def select_by_less_than_pivot_price(connection, pivot_price):
    '''allows user to select and show only games below or equal to a chosen price threshold'''

    try:
        cursor = connection.cursor()
        query = "SELECT Games.Name, Games.Rating, Genres.Genre, Prices.Price, Sizes.Size FROM Games JOIN Genres ON Games.Genre_ID=Genres.ID JOIN Prices ON Games.Price_ID=Prices.ID JOIN Sizes ON Games.Size_ID=Sizes.ID WHERE Price_ID <= ?;"
        cursor.execute(query, (pivot_price,))
        results = cursor.fetchall()
        print(
            f"\n{'Name':<20}{'Rating [/10]':<20}{'Genre':<20}{'Price':<20}{'Size':<20}")
        for info in results:
            print(
                f"{info[0]:<20}{info[1]:<20}{info[2]:<20}{info[3]:<20}{info[4]:<20}")
    except Exception as error:
        traceback.print_exc()
        print("\nUh oh, something went wrong while trying to SELECT_BY_PRICE")


def select_by_less_or_equal_to_pivot_size(connection, pivot_size):
    '''allows user to select and show only games below or equal to a chosen size threshold'''

    try:
        cursor = connection.cursor()
        query = "SELECT Games.Name, Games.Rating, Genres.Genre, Prices.Price, Sizes.Size FROM Games JOIN Genres ON Games.Genre_ID=Genres.ID JOIN Prices ON Games.Price_ID=Prices.ID JOIN Sizes ON Games.Size_ID=Sizes.ID WHERE Size_ID <= ?;"
        cursor.execute(query, (pivot_size,))
        results = cursor.fetchall()
        print(
            f"\n{'Name':<20}{'Rating [/10]':<20}{'Genre':<20}{'Price':<20}{'Size':<20}")
        for info in results:
            print(
                f"{info[0]:<20}{info[1]:<20}{info[2]:<20}{info[3]:<20}{info[4]:<20}")
    except Exception as error:
        traceback.print_exc()
        print("\nUh oh, something went wrong while trying to SELECT_BY_SIZE")


def select_by_more_than_or_equal_to_pivot_rating(connection, pivot_rating):
    '''allows user to select and show only games above or equal to a chosen rating'''

    try:
        cursor = connection.cursor()
        query = "SELECT Games.Name, Games.Rating, Genres.Genre, Prices.Price, Sizes.Size FROM Games JOIN Genres ON Games.Genre_ID=Genres.ID JOIN Prices ON Games.Price_ID=Prices.ID JOIN Sizes ON Games.Size_ID=Sizes.ID WHERE Rating >= ?;"
        cursor.execute(query, (pivot_rating,))
        results = cursor.fetchall()
        print(
            f"\n{'Name':<20}{'Rating [/10]':<20}{'Genre':<20}{'Price':<20}{'Size':<20}")
        for info in results:
            print(
                f"{info[0]:<20}{info[1]:<20}{info[2]:<20}{info[3]:<20}{info[4]:<20}")
    except Exception as error:
        traceback.print_exc()
        print("\nUh oh, something went wrong while trying to SELECT_BY_RATING")


def select_by_genre(connection, chosen_genre):
    '''allows user to select and show only games in a chosen genre'''

    try:
        cursor = connection.cursor()
        query = "SELECT Games.Name, Games.Rating, Genres.Genre, Prices.Price, Sizes.Size FROM Games JOIN Genres ON Games.Genre_ID=Genres.ID JOIN Prices ON Games.Price_ID=Prices.ID JOIN Sizes ON Games.Size_ID=Sizes.ID WHERE Genre_ID == ?;"
        cursor.execute(query, (chosen_genre,))
        results = cursor.fetchall()
        print(
            f"\n{'Name':<20}{'Rating [/10]':<20}{'Genre':<20}{'Price':<20}{'Size':<20}")
        for info in results:
            print(
                f"{info[0]:<20}{info[1]:<20}{info[2]:<20}{info[3]:<20}{info[4]:<20}")
    except Exception as error:
        traceback.print_exc()
        print("\nUh oh, something went wrong while trying to SELECT_BY_GENRE")


def ask_for_int_value(string):
    '''function that sanitises user input to make sure that they enter a valid number into parts of my program which require integers, without crashing the program'''

    while True:
        try:
            integer_input = input(f"{string}")
            int(integer_input)

            return integer_input
        except:
            print("\n\nPLEASE ENTER A VALID NUMERICAL VALUE!\n")


def user_input_valid_check(lower_bound, upper_bound, user_value):
    '''function which checks to make sure that the user doesn't enter a value lower or higher than they are meant to'''

    if int(user_value) > upper_bound or int(user_value) < lower_bound:
        while True:
            retry_user_input = ask_for_int_value(
                f"\nPlease enter a valid value between {lower_bound} and {upper_bound}: ")
            if int(retry_user_input) <= upper_bound and int(retry_user_input) >= lower_bound:
                print("\nRetried input was successful!\n")
                return retry_user_input
    else:
        return user_value


while True:

    '''the main loop which runs the whole interface/program on repeat until the user exits it'''

    with sqlite3.connect(TARGET_DATABASE_FILE) as connection:

        # lets user decide what they want to do with the database (whether they want to view data, edit it, or sort it/isolate it)

        user_input = input(
            "\n>[1] Display games/game details\n>[2] Add a game to database\n>[3] Delete a game from database\n>[4] Update a game rating\n>[5] Order/sort games\n>[6] Select/isolate games\n>[7] Exit\n\n")

        if user_input == "1":

            # lets the user view the table, and decide whether they want to see the full table, or just a list of the games contained in it

            show_query = input(
                "\n>[1] to see the whole games table\n>[2] to list the games present in the table\n")
            if show_query == "1":

                # show table of games (shows labels instead of ID's so that it is user friendly)

                print("\nShowing video games:\n")
                show_games(connection)
            elif show_query == "2":

                # lists all games present in table

                print("\nListing video games:\n")
                list_games(connection)
            else:
                print("\nINVALID INPUT RECIEVED!\n")

        elif user_input == "2":

            # allows the user to add a new game to the table and provide all necessary details about it

            new_game_name = input(
                "\nPlease enter the name of the new game you would like to add: ")

            new_rating = ask_for_int_value(
                "Please enter the rating of the new game (number)\n> [0 is the lowest rating, 10 is the highest]:\n")
            new_rating = user_input_valid_check(0, 10, new_rating)

            new_size_ID = ask_for_int_value(
                "Please enter size ID of the new game (number): \n> 1 is small (0-10gb) \n> 2 is medium (10-30gb)\n> 3 is large (30-100gb)\n")
            new_size_ID = user_input_valid_check(1, 3, new_size_ID)

            new_price_ID = ask_for_int_value(
                "Please enter price ID of the new game (number): \n> 0 is free \n> 1 is cheap ($0-$10)\n> 2 is medium ($10-$40)\n> 3 is expensive ($40-$100)\n")
            new_price_ID = user_input_valid_check(0, 3, new_price_ID)

            new_genre_ID = ask_for_int_value(
                "Please enter genre ID of the new game (number): \n> 1 is FPS (First Person Shooter) \n> 2 is Adventure/RPG\n> 3 is Sandbox\n")
            new_genre_ID = user_input_valid_check(1, 3, new_genre_ID)

            add_game(connection, new_game_name, new_rating,
                     new_size_ID, new_price_ID, new_genre_ID)

        elif user_input == "3":

            # allows the user to delete a chosen game (by name)

            game_to_delete = input(
                "\nPlease enter the name of the game you would like to delete [CASE SENSITIVE]: ")
            delete_game(connection, game_to_delete)

        elif user_input == "4":

            # allows the user to change the ratings of a chosen game (by name as well)

            game_to_update = input(
                "\nPlease enter the name of the game you would like to change the rating of [CASE SENSITIVE]: ")

            updated_rating = ask_for_int_value(
                "Please enter new rating (number)\n> [0 is the lowest rating, 10 is the highest]: \n")
            updated_rating = user_input_valid_check(0, 10, updated_rating)

            update_game_rating(connection, game_to_update, updated_rating)

        elif user_input == "5":

            # allows the user to order games/prioritise them based on different criteria

            order_type = input(
                "\n> [1] to order games by price\n> [2] to order by size\n> [3] to order by rating\n> [4] to order by genre\n")
            if order_type == "1":
                print("\nOrdering games by price!\n")
                order_games_by_price(connection)
            elif order_type == "2":
                print("\nOrdering games by size!\n")
                order_games_by_size(connection)
            elif order_type == "3":
                print("\nOrdering games by rating!\n")
                order_games_by_rating(connection)
            elif order_type == "4":
                print("\nOrdering games by genre!\n")
                order_games_by_genre(connection)
            else:
                print("\nINVALID INPUT RECIEVED!\n")

        elif user_input == "6":

            # allows the user to select/isolate games based on certain chosen criteria

            select_choice = input(
                "\n> [1] to select games less than or equal to a chosen size bracket\n> [2] to select games less than or equal to a chosen price bracket\n> [3] to select games above or equal to a chosen rating\n> [4] to select games by a in a specific genre\n")

            if select_choice == "1":
                chosen_pivot = ask_for_int_value(
                    "\nPlease enter your chosen number to select by: \n> 1 is small (0-10gb) \n> 2 is medium (10-30gb)\n> 3 is large (30-100gb)\n")
                chosen_pivot = user_input_valid_check(1, 3, chosen_pivot)

                print(
                    f"\nSelecting by size (less than / equal to size ID of {chosen_pivot}\n")

                select_by_less_or_equal_to_pivot_size(connection, chosen_pivot)
            elif select_choice == "2":
                chosen_pivot = ask_for_int_value(
                    "\nPlease enter your chosen number to select by: \n> 0 is free \n> 1 is cheap ($0-$10)\n> 2 is medium ($10-$40)\n> 3 is expensive ($40-$100)\n")
                chosen_pivot = user_input_valid_check(0, 3, chosen_pivot)

                print(
                    f"\nSelecting by price! (less than / equal to price ID of {chosen_pivot})")

                select_by_less_than_pivot_price(connection, chosen_pivot)
            elif select_choice == "3":
                chosen_pivot = ask_for_int_value(
                    "\nPlease enter your chosen number to select by: \n> [0 is the lowest rating, 10 is the highest]:\n")
                chosen_pivot = user_input_valid_check(0, 10, chosen_pivot)

                print(
                    f"\nSelecting by rating! (greater than / equal to rating of {chosen_pivot})")

                select_by_more_than_or_equal_to_pivot_rating(
                    connection, chosen_pivot)
            elif select_choice == "4":
                chosen_genre = ask_for_int_value(
                    "\nPlease enter your chosen genre ID to select by: \n> 1 is FPS \n> 2 is Adventure/RPG\n> 3 is Sandbox\n")
                chosen_genre = user_input_valid_check(1, 3, chosen_genre)

                print(f"\nSelecting by genre ID of {chosen_genre}!")

                select_by_genre(connection, chosen_genre)
            else:
                print("\nINVALID INPUT RECIEVED!\n")

        elif user_input == "7":

            # allows the user to easily exit the program when they want to

            print("\nEXITING NOW! Thank you for using my games database!\n")
            break

        else:

            # catches any invalid inputs and repeatedly asks for input until a valid input is recieved

            print(
                "\nPlease enter options 1, 2, 3, 4, 5, 6, or 7 (INVALID INPUT RECIEVED!)\n")
