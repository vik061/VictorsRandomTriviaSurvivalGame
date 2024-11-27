from unittest import TestCase

from game import is_level_up


class Test(TestCase):
    def test_is_level_up_false_character_level_1_xp_is_not_minimum_number_to_level_up(self):
        expected = False
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Level": 1, "XP": 0}
        actual = is_level_up(character)
        self.assertEqual(expected, actual)

    def test_is_level_up_true_character_level_1_xp_is_minimum_number_to_level_up(self):
        expected = True
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Level": 1, "XP": 2}
        actual = is_level_up(character)
        self.assertEqual(expected, actual)

    def test_is_level_up_false_character_level_2_xp_is_not_minimum_number_to_level_up(self):
        expected = False
        character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5, "Level": 2, "XP": 2}
        actual = is_level_up(character)
        self.assertEqual(expected, actual)

    def test_is_level_up_true_character_level_2_xp_is_minimum_number_to_level_up(self):
        expected = True
        character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5, "Level": 2, "XP": 3}
        actual = is_level_up(character)
        self.assertEqual(expected, actual)

    def test_is_level_up_false_character_level_3_xp_is_0(self):
        expected = False
        character = {"X-coordinate": 4, "Y-coordinate": 3, "Current HP": 5, "Level": 3, "XP": 0}
        actual = is_level_up(character)
        self.assertEqual(expected, actual)

    def test_is_level_up_false_character_level_3_xp_is_greater_than_0(self):
        expected = False
        character = {"X-coordinate": 4, "Y-coordinate": 3, "Current HP": 5, "Level": 3, "XP": 3}
        actual = is_level_up(character)
        self.assertEqual(expected, actual)
