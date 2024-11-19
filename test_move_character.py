from unittest import TestCase

from game import move_character


class Test(TestCase):
    def test_move_character_up(self):
        expected = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5, "Level": 1, "XP": 0}
        actual = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Level": 1, "XP": 0, "Direction": "Up"}
        move_character(actual)
        self.assertEqual(expected, actual)

    def test_move_character_down(self):
        expected = {"X-coordinate": 1, "Y-coordinate": 2, "Current HP": 5, "Level": 1, "XP": 0}
        actual = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Level": 1, "XP": 0, "Direction": "Down"}
        move_character(actual)
        self.assertEqual(expected, actual)

    def test_move_character_right(self):
        expected = {"X-coordinate": 2, "Y-coordinate": 1, "Current HP": 5, "Level": 1, "XP": 0}
        actual = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Level": 1, "XP": 0, "Direction": "Right"}
        move_character(actual)
        self.assertEqual(expected, actual)

    def test_move_character_left(self):
        expected = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5, "Level": 1, "XP": 0}
        actual = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Level": 1, "XP": 0, "Direction": "Left"}
        move_character(actual)
        self.assertEqual(expected, actual)
