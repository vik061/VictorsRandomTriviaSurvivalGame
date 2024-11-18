import io
from unittest import TestCase

from game import get_user_choice

from unittest.mock import patch


class Test(TestCase):
    @patch('builtins.input', return_value='w')
    def test_get_user_choice_valid_input_up(self, _):
        expected = 'Up'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='s')
    def test_get_user_choice_valid_input_down(self, _):
        expected = 'Down'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='a')
    def test_get_user_choice_valid_input_left(self, _):
        expected = 'Left'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='d')
    def test_get_user_choice_valid_input_right(self, _):
        expected = 'Right'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['aa', 's'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid_input_string_then_valid_direction(self, mock_output, _):
        expected = 'Not a valid direction. Enter a valid direction from the directions dictionary.\n'
        get_user_choice()
        actual = mock_output.getvalue()
        self.assertTrue(expected in actual)

    @patch('builtins.input', side_effect=[1, 's'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid_input_data_type_then_valid_direction(self, mock_output, _):
        expected = 'Not a valid direction type. Enter a valid direction from the directions dictionary.\n'
        get_user_choice()
        actual = mock_output.getvalue()
        self.assertTrue(expected in actual)
