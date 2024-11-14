from unittest import TestCase

from game import make_board


class Test(TestCase):
    def test_make_board_one_row_by_one_column(self):
        expected = {(0, 0): 'Start (no difficulty level)'}
        rows = 1
        columns = 1
        actual = make_board(rows, columns)
        self.assertEqual(expected, actual)

    def test_make_board_one_row_by_two_columns(self):
        expected = {(0, 0): 'Start (no difficulty level)', (0, 1): 'Easy'}
        rows = 1
        columns = 2
        actual = make_board(rows, columns)
        self.assertEqual(expected, actual)

    def test_make_board_three_rows_by_three_columns(self):
        expected = {
            (0, 0): 'Start (no difficulty level)', (0, 1): 'Easy', (0, 2): 'Easy',
            (1, 0): 'Easy', (1, 1): 'Easy', (1, 2): 'Easy',
            (2, 0): 'Easy', (2, 1): 'Easy', (2, 2): 'Medium',
        }
        rows = 3
        columns = 3
        actual = make_board(rows, columns)
        self.assertEqual(expected, actual)

    def test_make_board_five_rows_by_five_columns(self):
        expected = {
            (0, 0): 'Start (no difficulty level)', (0, 1): 'Easy', (0, 2): 'Easy', (0, 3): 'Easy', (0, 4): 'Medium',
            (1, 0): 'Easy', (1, 1): 'Easy', (1, 2): 'Easy', (1, 3): 'Medium', (1, 4): 'Hard',
            (2, 0): 'Easy', (2, 1): 'Easy', (2, 2): 'Medium', (2, 3): 'Medium', (2, 4): 'Hard',
            (3, 0): 'Medium', (3, 1): 'Medium', (3, 2): 'Medium', (3, 3): 'Hard', (3, 4): 'Very Hard',
            (4, 0): 'Medium', (4, 1): 'Medium', (4, 2): 'Hard', (4, 3): 'Very hard', (4, 4): 'Final Boss',
        }
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        self.assertEqual(expected, actual)
