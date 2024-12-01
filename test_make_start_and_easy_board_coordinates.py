from unittest import TestCase

from game import make_start_and_easy_board_coordinates


class Test(TestCase):
    def test_make_start_and_easy_board_coordinates(self):
        expected = {(0, 0): 'Start (no difficulty level)', (0, 1): 'Easy', (0, 2): 'Easy', (0, 3): 'Easy',
                    (1, 0): 'Easy', (1, 1): 'Easy', (1, 2): 'Easy', (2, 0): 'Easy', (2, 1): 'Easy'}
        rows = 5
        columns = 5
        actual = make_start_and_easy_board_coordinates(rows, columns)
        self.assertEqual(expected, actual)

    def test_make_start_and_easy_board_coordinates_has_start_string(self):
        expected = 'Start (no difficulty level)'
        rows = 5
        columns = 5
        actual = make_start_and_easy_board_coordinates(rows, columns)
        self.assertTrue(expected in actual.values())

    def test_make_start_and_easy_board_coordinates_has_easy_string(self):
        expected = 'Easy'
        rows = 5
        columns = 5
        actual = make_start_and_easy_board_coordinates(rows, columns)
        self.assertTrue(expected in actual.values())

    def test_make_start_and_easy_board_coordinates_has_start_coordinate(self):
        expected = (0, 0)
        rows = 5
        columns = 5
        actual = make_start_and_easy_board_coordinates(rows, columns)
        self.assertTrue(expected in actual)

    def test_make_start_and_easy_board_coordinates_has_an_easy_coordinate(self):
        expected = (1, 1)
        rows = 5
        columns = 5
        actual = make_start_and_easy_board_coordinates(rows, columns)
        self.assertTrue(expected in actual)
