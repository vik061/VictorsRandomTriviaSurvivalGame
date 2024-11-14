from unittest import TestCase

from game import make_character


class Test(TestCase):
    def test_make_character_has_x_coordinate(self):
        expected = "X-coordinate"
        actual = make_character()
        self.assertIn(expected, actual)

    def test_make_character_has_y_coordinate(self):
        expected = "Y-coordinate"
        actual = make_character()
        self.assertIn(expected, actual)

    def test_make_character_has_current_hp(self):
        expected = "Current HP"
        actual = make_character()
        self.assertIn(expected, actual)

    def test_make_character_has_level(self):
        expected = "Level"
        actual = make_character()
        self.assertIn(expected, actual)

    def test_make_character_has_xp(self):
        expected = "XP"
        actual = make_character()
        self.assertIn(expected, actual)

    def test_make_character_x_coordinate_is_0(self):
        expected = 0
        result = make_character()
        actual = result["X-coordinate"]
        self.assertEqual(expected, actual)

    def test_make_character_y_coordinate_is_0(self):
        expected = 0
        result = make_character()
        actual = result["Y-coordinate"]
        self.assertEqual(expected, actual)

    def test_make_character_current_hp_is_5(self):
        expected = 5
        result = make_character()
        actual = result["Current HP"]
        self.assertEqual(expected, actual)

    def test_make_character_level_is_1(self):
        expected = 1
        result = make_character()
        actual = result["Level"]
        self.assertEqual(expected, actual)

    def test_make_character_xp_is_0(self):
        expected = 0
        result = make_character()
        actual = result["XP"]
        self.assertEqual(expected, actual)
