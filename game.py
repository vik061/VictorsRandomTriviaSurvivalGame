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
    """
    pass


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
