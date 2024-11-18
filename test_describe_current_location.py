from unittest import TestCase

from game import make_board, make_character, describe_current_location


class Test(TestCase):
    def test_describe_current_location_at_start_coordinate(self):
        expected = 'Start (no difficulty level)'
        board = make_board(5, 5)
        character = make_character()
        actual = describe_current_location(board, character)
        self.assertEqual(expected, actual)

    def test_describe_current_location_at_easy_coordinate(self):
        expected = 'Easy'
        board = make_board(5, 5)
        character = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5, "Level": 1, "XP": 0}
        actual = describe_current_location(board, character)
        self.assertEqual(expected, actual)

    def test_describe_current_location_at_medium_coordinate(self):
        expected = 'Medium'
        board = make_board(5, 5)
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5, "Level": 1, "XP": 0}
        actual = describe_current_location(board, character)
        self.assertEqual(expected, actual)

    def test_describe_current_location_at_hard_coordinate(self):
        expected = 'Hard'
        board = make_board(5, 5)
        character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5, "Level": 1, "XP": 0}
        actual = describe_current_location(board, character)
        self.assertEqual(expected, actual)

    def test_describe_current_location_at_very_hard_coordinate(self):
        expected = 'Very Hard'
        board = make_board(5, 5)
        character = {"X-coordinate": 3, "Y-coordinate": 4, "Current HP": 5, "Level": 1, "XP": 0}
        actual = describe_current_location(board, character)
        self.assertEqual(expected, actual)

    def test_describe_current_location_at_final_boss_coordinate(self):
        expected = 'Final Boss'
        board = make_board(5, 5)
        character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5, "Level": 1, "XP": 0}
        actual = describe_current_location(board, character)
        self.assertEqual(expected, actual)
