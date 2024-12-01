from unittest import TestCase

from game import make_final_boss_board_coordinate


class Test(TestCase):
    def test_make_final_boss_board_coordinate(self):
        expected = {(4, 4): 'Final Boss'}
        rows = 5
        columns = 5
        actual = make_final_boss_board_coordinate(rows, columns)
        self.assertEqual(expected, actual)

    def test_make_final_boss_board_coordinate_has_final_boss_string(self):
        expected = 'Final Boss'
        rows = 5
        columns = 5
        actual = make_final_boss_board_coordinate(rows, columns)
        self.assertTrue(expected in actual.values())

    def test_make_final_boss_board_coordinate_has_final_boss_coordinate(self):
        expected = (4, 4)
        rows = 5
        columns = 5
        actual = make_final_boss_board_coordinate(rows, columns)
        self.assertTrue(expected in actual)
