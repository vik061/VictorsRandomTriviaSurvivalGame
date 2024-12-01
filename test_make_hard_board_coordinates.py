from unittest import TestCase

from game import make_hard_board_coordinates


class Test(TestCase):
    def test_make_hard_board_coordinates(self):
        expected = {(0, 4): 'Hard', (1, 4): 'Hard', (2, 4): 'Hard', (3, 3): 'Hard', (4, 2): 'Hard'}
        rows = 5
        columns = 5
        actual = make_hard_board_coordinates(rows, columns)
        self.assertEqual(expected, actual)

    def test_make_hard_board_coordinates_has_hard_string(self):
        expected = "Hard"
        rows = 5
        columns = 5
        actual = make_hard_board_coordinates(rows, columns)
        self.assertTrue(expected in actual.values())

    def test_make_hard_board_coordinates_has_a_hard_coordinate(self):
        expected = (4, 2)
        rows = 5
        columns = 5
        actual = make_hard_board_coordinates(rows, columns)
        self.assertTrue(expected in actual)
