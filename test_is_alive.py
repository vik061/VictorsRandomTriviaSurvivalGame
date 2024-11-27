from unittest import TestCase

from game import is_alive


class Test(TestCase):
    def test_is_alive_true_character_not_achieved_goal_with_more_than_1_HP(self):
        expected = True
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Level": 1, "XP": 0}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_is_alive_true_character_not_achieved_goal_with_1_HP(self):
        expected = True
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 1, "Level": 1, "XP": 0}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_is_alive_false_character_not_achieved_goal_with_0_HP(self):
        expected = False
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 0, "Level": 1, "XP": 0}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_is_alive_true_character_achieved_goal_with_more_than_1_HP(self):
        expected = True
        character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5, "Level": 3, "XP": 0}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_is_alive_true_character_achieved_goal_with_1_HP(self):
        expected = True
        character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 1, "Level": 3, "XP": 0}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_is_alive_false_character_achieved_goal_with_0_HP(self):
        expected = False
        character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 0, "Level": 3, "XP": 0}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

