from unittest import TestCase

from game import validate_move, make_board


class Test(TestCase):
    def test_validate_move_true_direction_up(self):
        expected = True
        board = make_board(5, 5)
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5, 'Level': 1, 'XP': 0}
        direction = "Up"
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_true_direction_down(self):
        expected = True
        board = make_board(5, 5)
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5, 'Level': 1, 'XP': 0}
        direction = "Down"
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_true_direction_right(self):
        expected = True
        board = make_board(5, 5)
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5, 'Level': 1, 'XP': 0}
        direction = "Right"
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_true_direction_left(self):
        expected = True
        board = make_board(5, 5)
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5, 'Level': 1, 'XP': 0}
        direction = "Left"
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_false_direction_up(self):
        expected = False
        board = make_board(5, 5)
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5, 'Level': 1, 'XP': 0}
        direction = "Up"
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_false_direction_down(self):
        expected = False
        board = make_board(5, 5)
        character = {'X-coordinate': 4, 'Y-coordinate': 0, 'Current HP': 5, 'Level': 1, 'XP': 0}
        direction = "Down"
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_false_direction_right(self):
        expected = False
        board = make_board(5, 5)
        character = {'X-coordinate': 0, 'Y-coordinate': 4, 'Current HP': 5, 'Level': 1, 'XP': 0}
        direction = "Up"
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_false_direction_left(self):
        expected = False
        board = make_board(5, 5)
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5, 'Level': 1, 'XP': 0}
        direction = "Left"
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)
