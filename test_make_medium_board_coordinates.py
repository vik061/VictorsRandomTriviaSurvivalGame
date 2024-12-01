from unittest import TestCase

from game import make_medium_board_coordinates


class Test(TestCase):
    def test_make_medium_board_coordinates(self):
        expected = {(0, 4): 'Medium', (1, 3): 'Medium', (2, 2): 'Medium', (2, 3): 'Medium', (3, 0): 'Medium', \
                    (3, 1): 'Medium', (3, 2): 'Medium', (4, 0): 'Medium', (4, 1): 'Medium'}
        rows = 5
        columns = 5
        actual = make_medium_board_coordinates(rows, columns)
        self.assertEqual(expected, actual)

    def test_make_medium_board_coordinates_has_medium_string(self):
        expected = 'Medium'
        rows = 5
        columns = 5
        actual = make_medium_board_coordinates(rows, columns)
        self.assertTrue(expected in actual.values())

    def test_make_medium_board_coordinates_has_a_medium_coordinate(self):
        expected = (4, 0)
        rows = 5
        columns = 5
        actual = make_medium_board_coordinates(rows, columns)
        self.assertTrue(expected in actual)
