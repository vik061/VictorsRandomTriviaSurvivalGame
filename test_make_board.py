from unittest import TestCase

from game import make_board


class Test(TestCase):
    def test_make_board_one_row_by_one_column(self):
        expected = {(0, 0): 'Start (no difficulty level)', (0, 1): 'Easy', (0, 2): 'Easy', (0, 3): 'Easy',
                    (1, 0): 'Easy', (1, 1): 'Easy', (1, 2): 'Easy', (2, 0): 'Easy', (2, 1): 'Easy', (0, 4): 'Hard',
                    (1, 3): 'Medium', (2, 2): 'Medium', (2, 3): 'Medium', (3, 0): 'Medium', (3, 1): 'Medium',
                    (3, 2): 'Medium', (4, 0): 'Medium', (4, 1): 'Medium', (1, 4): 'Hard', (2, 4): 'Hard',
                    (3, 3): 'Hard', (4, 2): 'Hard', (3, 4): 'Very Hard', (4, 3): 'Very Hard', (4, 4): 'Final Boss'}
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        self.assertEqual(expected, actual)

    def test_make_board_has_start_string(self):
        expected = 'Start (no difficulty level)'
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        self.assertTrue(expected in actual.values())

    def test_make_board_has_start_coordinate(self):
        expected = (0, 0)
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        self.assertTrue(expected in actual)

    def test_make_board_has_easy_string(self):
        expected = 'Easy'
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        self.assertTrue(expected in actual.values())

    def test_make_board_has_an_easy_coordinate(self):
        expected = (1, 1)
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        self.assertTrue(expected in actual)

    def test_make_board_has_medium_string(self):
        expected = 'Medium'
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        self.assertTrue(expected in actual.values())

    def test_make_board_has_a_medium_coordinate(self):
        expected = (4, 0)
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        self.assertTrue(expected in actual)

    def test_make_board_has_hard_string(self):
        expected = 'Hard'
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        self.assertTrue(expected in actual.values())

    def test_make_board_has_a_hard_coordinate(self):
        expected = (4, 2)
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        self.assertTrue(expected in actual)

    def test_make_board_has_very_hard_string(self):
        expected = 'Very Hard'
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        self.assertTrue(expected in actual.values())

    def test_make_board_has_a_very_hard_coordinate(self):
        expected = (4, 3)
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        self.assertTrue(expected in actual)

    def test_make_board_has_final_boss_string(self):
        expected = 'Final Boss'
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        self.assertTrue(expected in actual.values())

    def test_make_board_has_a_final_boss_coordinate(self):
        expected = (4, 4)
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        self.assertTrue(expected in actual)
