from unittest import TestCase

from game import check_if_goal_attained, make_board


class Test(TestCase):
    def test_check_if_goal_attained_false_character_at_start(self):
        expected = False
        board = make_board(5, 5)
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Level": 1, "XP": 0}
        actual = check_if_goal_attained(board, character)
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_false_character_at_max_x_coordinate_zero_y_coordinate(self):
        expected = False
        board = make_board(5, 5)
        character = {"X-coordinate": 4, "Y-coordinate": 0, "Current HP": 5, "Level": 1, "XP": 0}
        actual = check_if_goal_attained(board, character)
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_false_character_at_zero_x_coordinate_max_y_coordinate(self):
        expected = False
        board = make_board(5, 5)
        character = {"X-coordinate": 0, "Y-coordinate": 4, "Current HP": 5, "Level": 1, "XP": 0}
        actual = check_if_goal_attained(board, character)
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_false_character_at_not_finished_non_zeros_coordinate(self):
        expected = False
        board = make_board(5, 5)
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Level": 1, "XP": 0}
        actual = check_if_goal_attained(board, character)
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_false_character_almost_at_finished_coordinate(self):
        expected = False
        board = make_board(5, 5)
        character = {"X-coordinate": 4, "Y-coordinate": 3, "Current HP": 5, "Level": 1, "XP": 0}
        actual = check_if_goal_attained(board, character)
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_true_at_finished_coordinate_at_1_HP(self):
        expected = True
        board = make_board(5, 5)
        character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5, "Level": 1, "XP": 0}
        actual = check_if_goal_attained(board, character)
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_false_at_finished_coordinate_at_0_HP(self):
        expected = False
        board = make_board(5, 5)
        character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 0, "Level": 1, "XP": 0}
        actual = check_if_goal_attained(board, character)
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_false_character_at_not_finished_coordinate_at_0_HP(self):
        expected = False
        board = make_board(5, 5)
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 0, "Level": 1, "XP": 0}
        actual = check_if_goal_attained(board, character)
        self.assertEqual(expected, actual)
