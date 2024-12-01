from unittest import TestCase

from game import make_very_hard_board_coordinates


class Test(TestCase):
    def test_make_very_hard_board_coordinates(self):
        expected = {(3, 4): 'Very Hard', (4, 3): 'Very Hard'}
        rows = 5
        columns = 5
        actual = make_very_hard_board_coordinates(rows, columns)
        self.assertEqual(expected, actual)

    def test_make_very_hard_board_coordinates_has_very_hard_string(self):
        expected = 'Very Hard'
        rows = 5
        columns = 5
        actual = make_very_hard_board_coordinates(rows, columns)
        self.assertTrue(expected in actual.values())

    def test_make_very_hard_board_coordinates_has_very_hard_coordinate(self):
        expected = (3, 4)
        rows = 5
        columns = 5
        actual = make_very_hard_board_coordinates(rows, columns)
        self.assertTrue(expected in actual)
