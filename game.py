import random


def make_board(rows, columns):
    """
    Create a game board with the given number of rows and columns.

    Each coordinate on the board has a string describing the difficulty level.
    For my game, assume that the game board will have 5 rows and 5 columns.

    :param rows: an integer
    :param columns: an integer
    :precondition: rows and columns must be positive non-zero integers
    :precondition: for the purpose of my game, rows and columns must be less than or equal to five
    :postcondition: create a game board with the given number of rows and columns
    :return: a dictionary with each key as a tuple with a set of coordinates, and
    each value as a short string description of the difficulty level

    >>> rows_example_one = 1
    >>> columns_example_one = 1
    >>> board = make_board(rows_example_one, columns_example_one)
    >>> board
    {(0, 0): 'Start (no difficulty level)'}
    >>> rows_example_two = 2
    >>> columns_example_two = 2
    >>> board = make_board(rows_example_two, columns_example_two)
    >>> board
    {(0, 0): 'Start (no difficulty level)', (0, 1): 'Easy', (1, 0): 'Easy', (1, 1): 'Easy'}
    """
    board_dictionary = {}
    board_difficulty_levels_list = ['Start (no difficulty level)', 'Easy', 'Medium', 'Hard', 'Very Hard', 'Final Boss']

    for row_coordinate in range(rows):
        for column_coordinate in range(columns):
            if row_coordinate == 0 and column_coordinate == 0:
                board_dictionary[(row_coordinate, column_coordinate)] = board_difficulty_levels_list[0]
            elif (row_coordinate == 0 and column_coordinate <= 3) \
                    or (row_coordinate == 1 and column_coordinate <= 2) \
                    or (row_coordinate == 2 and column_coordinate <= 1):
                board_dictionary[(row_coordinate, column_coordinate)] = board_difficulty_levels_list[1]
            elif (row_coordinate == 0 and column_coordinate == 4) \
                    or (row_coordinate == 1 and column_coordinate == 3) \
                    or (row_coordinate == 2 and 2 <= column_coordinate <= 3) \
                    or (row_coordinate == 3 and column_coordinate <= 2) \
                    or (row_coordinate == 4 and column_coordinate <= 1):
                board_dictionary[(row_coordinate, column_coordinate)] = board_difficulty_levels_list[2]
            elif (row_coordinate <= 2 and column_coordinate == 4) \
                    or (row_coordinate == 3 and column_coordinate == 3) \
                    or (row_coordinate == 4 and column_coordinate == 2):
                board_dictionary[(row_coordinate, column_coordinate)] = board_difficulty_levels_list[3]
            elif (row_coordinate == 3 and column_coordinate == 4) \
                    or (row_coordinate == 4 and column_coordinate == 3):
                board_dictionary[(row_coordinate, column_coordinate)] = board_difficulty_levels_list[4]
            elif row_coordinate == 4 and column_coordinate == 4:
                board_dictionary[(row_coordinate, column_coordinate)] = board_difficulty_levels_list[5]

    return board_dictionary


def make_character():
    """
    Create a character for the game at the starting coordinate.

    :return: a dictionary with the following key-pair coordinates:
    "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Level": 1, "XP": 0

    >>> player = make_character()
    >>> player
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5, 'Level': 1, 'XP': 0}
    """
    return {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Level": 1, "XP": 0}


def describe_current_location(board, character):
    """
    Describe the current location of the character on the board.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: character's X- and Y-coordinates are within the board's range of values
    :postcondition: describe the current location of the character on the board
    :print: a string with a short description of the character's current location on the board

    >>> board_example_one = make_board(5, 5)
    >>> character_example_one = make_character()
    >>> describe_current_location(board_example_one, character_example_one)
    Start (no difficulty level)
    >>> board_example_one = make_board(5, 5)
    >>> character_example_one = {"X-coordinate": 3, "Y-coordinate": 4, "Current HP": 5, "Level": 1, "XP": 0}
    >>> describe_current_location(board_example_one, character_example_one)
    Very Hard
    """
    print(board[character["X-coordinate"], character["Y-coordinate"]])


def get_user_choice():
    """
    Get the player's inputted direction choice from a printed dictionary of directions.

    The player gets a printed warning message if they input an invalid direction choice.

    :return: a string with the player's valid inputted direction choice
    """
    directions_dict = {1: 'Up', 2: 'Down', 3: 'Left', 4: 'Right'}
    print(directions_dict)

    while True:
        try:
            user_choice = int(input("Enter a direction: "))
            if user_choice in directions_dict:
                return directions_dict[user_choice]
            else:
                raise ValueError
        except ValueError:
            print("Not a valid direction. Enter a valid direction from the directions dictionary.\n")
            print(directions_dict)
            continue


def validate_move(board, character, direction):
    """
    Check whether the player's direction is a valid move.

    Check if the player's direction goes outside the board based on their character's current coordinates.

    :param board: a dictionary
    :param character: a dictionary
    :param direction: a string
    :precondition: character has valid X- and Y-coordinates
    :precondition: direction is either "Up", "Down", "Left" or "Right"
    :postcondition: check whether the player's direction is a valid move
    :return: a Boolean value asserting the player's move on the board

    >>> board_example_one = make_board(5, 5)
    >>> character_example_one = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5, 'Level': 1, 'XP': 0}
    >>> direction_example_one = "Up"
    >>> validate_move(board_example_one, character_example_one, direction_example_one)
    False
    >>> board_example_one = make_board(5, 5)
    >>> character_example_one = {'X-coordinate': 3, 'Y-coordinate': 3, 'Current HP': 5, 'Level': 1, 'XP': 0}
    >>> direction_example_one = "Right"
    >>> validate_move(board_example_one, character_example_one, direction_example_one)
    True
    """
    board_coordinates = board.keys()
    max_board_coordinates = max(board_coordinates)

    if (direction == "Up" and character["Y-coordinate"] == 0) \
            or (direction == "Down" and character["Y-coordinate"] == max_board_coordinates[1]) \
            or (direction == "Right" and character["X-coordinate"] == max_board_coordinates[0]) \
            or (direction == "Left" and character["X-coordinate"] == 0):
        return False

    character['Direction'] = direction
    return True


def move_character(character):
    """
    Update the character's X- or Y- coordinate according to the player's valid direction.

    In other words, move the player's character in a valid direction to a different coordinate.

    :param character: a dictionary
    :precondition: character has a valid 'X-coordinate' and 'Y-coordinate' key value pair
    :precondition: character has a 'Direction' key with a value consisting of one of the four valid directions
    ("Up", "Down", "Right", "Left")
    :postcondition: update the character's X- or Y- coordinate according to the player's direction
    """
    if character['Direction'] == "Up":
        character['Y-coordinate'] -= 1
    elif character['Direction'] == "Down":
        character['Y-coordinate'] += 1
    elif character['Direction'] == "Right":
        character['X-coordinate'] += 1
    elif character['Direction'] == "Left":
        character['X-coordinate'] -= 1

    del character['Direction']


def trivia_topics():
    """
    Group trivia topics into a difficulty level list and compile each difficulty list into one compiled list.

    :return: a list of the compiled trivia topics grouped by difficulty level
    """
    random_letter = [random.choice(['a', 'b', 'c']), "Guess a random letter: choices are 'a', 'b', 'c', 'd', 'e'.\n",
                     "Level 2 Hint: the correct answer is not 'd'.\n",
                     "Level 3 Hint: the correct answer is not 'e' or 'd'.\n"]

    ag_members = [{'b', 'B'},
                  ("Atarashii Gakko! is a Japanese girl group with four members.What are the names of each member?\n"
                   "a. Mizu, Rina, Shizuka, Kannon\n"
                   "b. Mizyu, Rin, Suzuka, Kanon\n"
                   "c. Miziu, Rinn, Suezuka, Kanon\n"
                   "d. Miyzu, Rinna, Shuzuka, Kahnon\n "
                   ), "Level 2 Hint: the correct answer is not d\n",
                  "Level 3 Hint: the correct answers are not d nor c\n"]

    instruments = [{'t', 'T'},
                   "Choose T (True) or F (False) for the following statement:\nI can play the piano, clarinet, "
                   "and tenor saxophone.\n",
                   "Level 2 Hint: I learned to play the piano first, and the music skills I learned from playing the "
                   "piano can be transferred to other instruments.\n",
                   "Level 3 Hint: I played in my high school’s concert and jazz band. There’s a good chance I played "
                   "the instruments mentioned in the True/False statement.\n"]

    figure_skating = [{'t', 'T'},
                      "Choose T (True) or F (False) for the following statement:\nI am a Canadian national medalist "
                      "in the pairs discipline in figure skating.\n",
                      "Level 2 Hint: I used to be a competitive figure skater in the singles and pairs discipline in "
                      "Canada.\n",
                      "Level 3 Hint: You can find my name in Wikipedia’s “Canadian Figure Skating Championships”. "
                      "It’s up to you to find which year, assuming that this hint is telling you the truth ;) \n"]

    free_pass = ['1',
                 "You moved to a very easy space! Guess a number between 1 and 1 inclusive and move on with my "
                 "game!\n",
                 "Level 2 Hint: Keep it simple. Less overthinking, more simplicity.\n",
                 "Level 3 Hint: Just enter 1 for your input. Please, enter 1\n"]

    soil = [{'f', 'F'},
            "Choose T (True) or F (False) for the following statement:\nSoil is the same thing as dirt.\n",
            "Level 2 Hint: Think about where you find soil versus dirt.\n",
            "Level 3 Hint: Soil is a natural layer of earth often found with living plants and organisms. Does dirt "
            "have all the same features as soil?\n"]

    twice = [{'d', 'D'},
             ("In which city/cities did K-pop girl group TWICE film their music video for “Likey”?\n"
              "a. Vancouver\n"
              "b. Richmond\n"
              "c. White Rock\n"
              "d. All of the above\n "
              ),
             "Level 2 Hint: TWICE did film their music video in Vancouver, BC, but is that the only “city”?\n",
             "Level 3 Hint: TWICE did film a part of their music video in Steveston. If you know where Steveston is, "
             "you might as well have the answer to this question.\n"]

    python = [{'t', 'T'},
              "Choose T (True) or F (False) for the following statement:\nPython is a dynamically typed language.\n",
              "Level 2 Hint: Think about the “+” operator in Python. What can it do? Is it restricted to only one "
              "data type?\n",
              "Level 3 Hint: If we have a program with two variables, a, and b, and we do a + b, do we have to "
              "declare the data type before each variable before running the program in Python?\n"]

    countries = [{'a', 'A'},
                 ("Which country have I yet to visit (as of November 2024)?\n"
                  "a. Belgium\n"
                  "b. Russia\n"
                  "c. South Korea\n"
                  "d. Vatican City\n "
                  ),
                 "Level 2 Hint: I visited Vatican City while I was travelling in Italy in the early 2010s.\n",
                 "Level 3 Hint: I visited Vatican City in the early 2010s and South Korea in August 2024.\n"]

    bc_team = ['4',
               "Final Boss question: How many times have I been included in the BC/YK provincial team in figure "
               "skating?\n Enter an integer (if you don’t know the answer, enter your best integer guess).\n",
               "Level 2 Hint: The number is between 1 and 5 inclusive.\n",
               "Level 3 Hint: The number is between 2 and 4 inclusive.\n"]

    itzy = [{'f', 'F'},
            "Choose T (True) or F (False) for the following statement:\nJust like the number of letters in ITZY, "
            "a K-pop girl group, ITZY currently has 4 members as of November 2024.\n",
            "Level 2 Hint: ITZY has a few songs with “(Final Version)” after the song title. Could this be related to "
            "the number of members at different times?\n",
            "Level 3 Hint: ITZY had a fan meeting in Seoul in early November 2024. How many members can be seen on "
            "the promotional posters of this fan meeting?\n"]

    food = [{'a', 'A'},
            ("What is my favourite food?\n"
             "a. Sushi\n"
             "b. Sashimi (fresh raw fish or meat)\n"
             "c. Shawarma\n"
             "d. None of the above\n"
             ),
            "Level 2 Hint: I enjoy one of the foods mentioned above. In other words, the correct answer is not d.\n",
            "Level 3 Hint: The correct answer is not d. As of November 2024, sashimi is not my favourite food. It "
            "makes my stomach upset :( \n"]

    translation = ['pizza',
                   "Translate the English word “pizza” to Danish using lowercase letters only.\n",
                   "Level 2 Hint: Try not to overthink and keep it simple! Other languages have very similar or the "
                   "same words as pizza.\n",
                   "Level 3 Hint: “Pizza” is also called “pizza” in other languages, such as French, Italian ("
                   "obviously), and Swedish.\n"]

    provinces = [{'d', 'D'},
                 ("Which Canadian province(s) have I not visited as of November 2024?\n"
                  "a. Quebec\n"
                  "b. Saskatchewan\n"
                  "c. Both a and b\n"
                  "d. None of the above\n"
                  ),
                 "Level 2 Hint: The correct answer is not c.\n",
                 "Level 3 Hint: I have been to Quebec for a national level figure skating competition. In other words, "
                 "the incorrect answers are a and c\n"]

    forest_fires = [{'t', 'T'},
                    "Choose T (True) or F (False) for the following statement:\nRegarding long-term forest health, "
                    "it’s better to have no fires in forests instead of doing prescribed (controlled) burns.\n",
                    "Level 2 Hint: Think about what would happen if a forest had a big fire in the future. Would the "
                    "forest with no past fires have less area destroyed than the forest with prescribed burn?\n",
                    "Level 3 Hint: Forests with longer gaps between fires usually do way worse when there’s a future "
                    "forest fire because their (plant) species have not developed the proper resilience to fire.\n"]

    hockey = [{'f', 'F'},
              "Choose T (True) or F (False) for the following statement:\nAs the first part of the team name "
              "suggests, the WHL hockey team “Vancouver Giants” is playing in the City of Vancouver as of November "
              "2024.\n",
              "Level 2 Hint: The Vancouver Giants play in Metro Vancouver.\n",
              "Level 3 Hint:  The Vancouver Giants used to play at the Pacific Coliseum in Vancouver. Emphasis on "
              "“used to.”\n"]

    le_sserafim = [{'b', 'B'},
                   (
                       "Le Sserafim is a (formerly six) five-member K-pop girl group under Source Music, a subsidiary "
                       "of which entertainment company?\n"
                       "a. JYP Entertainment\n"
                       "b. HYBE Corporation\n"
                       "c. SM Entertainment\n"
                       "d. YG Entertainment\n"
                   ),
                   "Level 2 Hint: Le Sserafim is not associated with JYP Entertainment (a is incorrect).\n",
                   "Level 3 Hint: Le Sserafim is not associated with JYP Entertainment nor SM Entertainment (a and c "
                   "are incorrect).\n"]

    stitches = [{'t', 'T'},
                "Choose T (True) or F (False) for the following statement:\nI had stitches on my leg when I was "
                "13 years old.\n",
                "Level 2 Hint: I got three stitches just below my left kneecap, assuming that I’m telling you the "
                "truth ;)\n",
                "Level 3 Hint: I can tell you how I got those stitches because I clearly remember the scene on "
                "that day. I still have a bruise on my leg. Again, assuming that I’m telling you the truth.\n"]

    rick_roll = ['down',
                 "Enter one word in lowercase only to finish this lyric:\n Never gonna give you up, never gonna let you"
                 " ____.\n",
                 "Level 2 Hint: This song was released in 1987 by an English singer, and is now a popular icon for "
                 "purposely redirecting people to this song’s YouTube video.\n",
                 "Level 3 Hint: The opposite word for up is …\n"]

    canucks = ['MILLER',
               "Enter one word IN UPPERCASE ONLY to complete this fan chant/cheer for a specific player on the "
               "Vancouver Canucks roster as of early November 2024:\n J.! T.! _____!\n",
               "Level 2 Hint: This player played for other NHL teams such as the Tampa Bay Lightning before being "
               "traded to the Canucks.\n",
               "Level 3 Hint: This player wears jersey number 9 for the Canucks as of early November 2024.\n"]

    crows = [{'d', 'D'},
             ("Which family do crows belong to?\n"
              "a. Coraciiformes\n"
              "b. Birdae\n"
              "c. Laridae\n"
              "d. Corvidae\n"),
             "Level 2 Hint: The correct is not Birdae.\n",
             "Level 3 Hint: The correct answers are not Birdae and Laridae\n"]

    airlines = [{'c', 'C'},
                ("As of November 2024, which airline company did I fly with at least once??\n"
                 "a. ITA Airways (Italy)\n"
                 "b. Korean Air (South Korea)\n"
                 "c. Aeromexico (Mexico)\n"
                 "d. British Airways (UK)\n"),
                "Level 2 Hint: I have never flown with ITA Airways as of November 2024.\n",
                "Level 3 Hint: I have never flown with ITA Airways nor Korean Air as of November 2024\n"]

    motorcycle = [{'t', 'T'},
                  "Choose T (True) or F (False) for the following statement:\nI can’t drive a motorcycle.\n",
                  "Level 2 Hint: I only have one vehicle license.\n",
                  "Level 3 Hint: I can drive a vehicle with four wheels, but I’m unsure if a two-wheeled car exists. "
                  "If it exists, I could operate it.\n"]

    favourite_course = [{'t', 'T'},
                        "Choose T (True) or F (False) for the following statement:\nMy favourite course for Term 1 in "
                        "BCIT"
                        "CST at the Downtown Campus is COMP 1510 Programming Methods.\n",
                        "Level 2 Hint: Which other course lets me program a game using Python!? Not COMP 1537 Web "
                        "Development!\n",
                        "Level 3 Hint: This is not a trick question, Chris!\n"]

    easy_list = [free_pass, python, rick_roll, provinces, canucks, food, countries, translation]
    medium_list = [random_letter, soil, instruments, ag_members, hockey, twice, airlines, figure_skating, motorcycle]
    hard_list = [crows, itzy, stitches, favourite_course]
    very_hard_list = [le_sserafim, forest_fires]
    final_boss_list = [bc_team]

    trivia_list = [easy_list, medium_list, hard_list, very_hard_list, final_boss_list]

    return trivia_list


def choose_trivia_topic(level):
    """
    Choose a trivia topic randomly based on the given level.

    Remove the chosen trivia topic from the associated level's trivia questions list.

    :param level: a string
    :precondition: level is either "Easy", "Medium", "Hard", "Very Hard" or "Final Boss"
    :postcondition: choose a trivia topic randomly based on the given level
    :return: a list of the answer, question, and Level 2 and 3 hints of the chosen trivia topic
    """


def game():  # called from main
    """
    Play the game.
    """
    # template of game(), will change as I implement more functions
    # print("Welcome to Victor's game!\n Instructions go here.\n")
    # rows = 5
    # columns = 5
    # board = make_board(rows, columns)
    # character = make_character()
    # achieved_goal = False
    # while is_alive(character) and not achieved_goal:
    #     # Tell the user where they are
    #     describe_current_location(board, character)
    #     direction = get_user_choice()
    #     valid_move = validate_move(board, character, direction)
    #     if valid_move:
    #         move_character(character)
    #         trivia_level = describe_current_location(board, character)
    #         print("")
    #         trivia_topics() # gather trivia topics
    #         choose_trivia_topic()
    #         trivia_question()
    #       achieved_goal = check_if_goal_attained(board, character)
    #     else:
    #         # Tell the user they can’t go in that direction
    #         print("Not a valid move. You are going out of the game board!\n")

    #     # Print end of game stuff like congratulations or sorry you died
    # if character['Current HP'] == 0:
    #     print("You have no HP left. Game over.")
    # else:
    #     print("Congratulations! You completed Victor's Random Trivia Survival Game! Thanks for playing!")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
