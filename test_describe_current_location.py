from unittest import TestCase

from game import make_board, make_character, describe_current_location

from unittest.mock import patch


class Test(TestCase):
    @patch('builtins.print', return_value='Start (no difficulty level)')
    def test_describe_current_location_at_start_coordinate(self, _):
        expected = 'Start (no difficulty level)'
        board = make_board(5, 5)
        character = make_character()
        self.assertEqual(expected, print(describe_current_location(board, character)))

    @patch('builtins.print', return_value='Easy')
    def test_describe_current_location_at_easy_coordinate(self, _):
        expected = 'Easy'
        board = make_board(5, 5)
        character = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5, "Level": 1, "XP": 0}
        self.assertEqual(expected, print(describe_current_location(board, character)))

    @patch('builtins.print', return_value='Medium')
    def test_describe_current_location_at_medium_coordinate(self, _):
        expected = 'Medium'
        board = make_board(5, 5)
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5, "Level": 1, "XP": 0}
        self.assertEqual(expected, print(describe_current_location(board, character)))

    @patch('builtins.print', return_value='Hard')
    def test_describe_current_location_at_hard_coordinate(self, _):
        expected = 'Hard'
        board = make_board(5, 5)
        character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5, "Level": 1, "XP": 0}
        self.assertEqual(expected, print(describe_current_location(board, character)))

    @patch('builtins.print', return_value='Very Hard')
    def test_describe_current_location_at_very_hard_coordinate(self, _):
        expected = 'Very Hard'
        board = make_board(5, 5)
        character = {"X-coordinate": 3, "Y-coordinate": 4, "Current HP": 5, "Level": 1, "XP": 0}
        self.assertEqual(expected, print(describe_current_location(board, character)))

    @patch('builtins.print', return_value='Final Boss')
    def test_describe_current_location_at_final_boss_coordinate(self, _):
        expected = 'Final Boss'
        board = make_board(5, 5)
        character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5, "Level": 1, "XP": 0}
        self.assertEqual(expected, print(describe_current_location(board, character)))
