def make_board(rows, columns):
    """
    Create a game board with the given number of rows and columns.

    Each coordinate on the board has a string describing the difficulty level.

    :param rows: an integer
    :param columns: an integer
    :precondition: rows and columns must be positive non-zero integers
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


def game():  # called from main
    """
    Play the game.
    """
    # template of game(), will change as I implement more functions
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
    #         describe_current_location(board, character)
    #         print("")
    #         there_is_a_challenger = check_for_foes()
    #         if there_is_a_challenger:
    #             guessing_game(character)
    #         achieved_goal = check_if_goal_attained(board, character)
    #     else:
    #         # Tell the user they can’t go in that direction
    #         print("Not a valid move. You are going out of the game board!\n")
    #
    #     # Print end of game stuff like congratulations or sorry you died
    # if character['Current HP'] == 0:
    #     print("You have no HP left. Game over.")
    # else:
    #     print("Congratulations! You have completed the game!")
    pass


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
