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
