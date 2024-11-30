from unittest import TestCase

from game import verify_trivia_response


class Test(TestCase):
    def test_verify_trivia_response_correct_input_easy_level(self):
        expected = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Level": 1, "XP": 1}
        response = 'd'
        topic = [['d', 'D'],
                 ("Which Canadian province(s) have I not visited as of November 2024?\n"
                  "a. Quebec\n"
                  "b. Saskatchewan\n"
                  "c. Both a and b\n"
                  "d. None of the above\n"
                  ),
                 "Level 2 Hint: The correct answer is not c.\n",
                 "Level 3 Hint: I have been to Quebec for a national level figure skating "
                 "competition. In other words, the incorrect answers are a and c\n"]
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Level": 1, "XP": 0}
        actual = verify_trivia_response(response, topic, character)
        self.assertEqual(expected, actual)

    def test_verify_trivia_response_incorrect_input_easy_level(self):
        expected = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 4, "Level": 1, "XP": 0}
        response = 'c'
        topic = [['d', 'D'],
                 ("Which Canadian province(s) have I not visited as of November 2024?\n"
                  "a. Quebec\n"
                  "b. Saskatchewan\n"
                  "c. Both a and b\n"
                  "d. None of the above\n"
                  ),
                 "Level 2 Hint: The correct answer is not c.\n",
                 "Level 3 Hint: I have been to Quebec for a national level figure skating "
                 "competition. In other words, the incorrect answers are a and c\n"]
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Level": 1, "XP": 0}
        actual = verify_trivia_response(response, topic, character)
        self.assertEqual(expected, actual)

    def test_verify_trivia_response_correct_input_medium_level(self):
        expected = {"X-coordinate": 4, "Y-coordinate": 0, "Current HP": 5, "Level": 1, "XP": 1}
        response = 'F'
        topic = [['f', 'F'],
                 "Choose T (True) or F (False) for the following statement:\nSoil is the same thing as dirt.\n",
                 "Level 2 Hint: Think about where you find soil versus dirt.\n",
                 "Level 3 Hint: Soil is a natural layer of earth often found with living plants and organisms. Does "
                 "dirt have all the same features as soil?\n"]
        character = {"X-coordinate": 4, "Y-coordinate": 0, "Current HP": 5, "Level": 1, "XP": 0}
        actual = verify_trivia_response(response, topic, character)
        self.assertEqual(expected, actual)

    def test_verify_trivia_response_incorrect_input_medium_level(self):
        expected = {"X-coordinate": 4, "Y-coordinate": 0, "Current HP": 4, "Level": 1, "XP": 0}
        response = 'T'
        topic = [['f', 'F'],
                 "Choose T (True) or F (False) for the following statement:\nSoil is the same thing as dirt.\n",
                 "Level 2 Hint: Think about where you find soil versus dirt.\n",
                 "Level 3 Hint: Soil is a natural layer of earth often found with living plants and organisms. Does "
                 "dirt have all the same features as soil?\n"]
        character = {"X-coordinate": 4, "Y-coordinate": 0, "Current HP": 5, "Level": 1, "XP": 0}
        actual = verify_trivia_response(response, topic, character)
        self.assertEqual(expected, actual)

    def test_verify_trivia_response_correct_input_hard_level(self):
        expected = {"X-coordinate": 4, "Y-coordinate": 2, "Current HP": 5, "Level": 1, "XP": 1}
        response = 'd'
        topic = [['d', 'D'],
                 ("Which family do crows belong to?\n"
                  "a. Coraciiformes\n"
                  "b. Birdae\n"
                  "c. Laridae\n"
                  "d. Corvidae\n"),
                 "Level 2 Hint: The correct is not Birdae.\n",
                 "Level 3 Hint: The correct answers are not Birdae and Laridae\n"]
        character = {"X-coordinate": 4, "Y-coordinate": 2, "Current HP": 5, "Level": 1, "XP": 0}
        actual = verify_trivia_response(response, topic, character)
        self.assertEqual(expected, actual)

    def test_verify_trivia_response_incorrect_input_hard_level(self):
        expected = {"X-coordinate": 4, "Y-coordinate": 2, "Current HP": 4, "Level": 1, "XP": 0}
        response = 'b'
        topic = [['d', 'D'],
                 ("Which family do crows belong to?\n"
                  "a. Coraciiformes\n"
                  "b. Birdae\n"
                  "c. Laridae\n"
                  "d. Corvidae\n"),
                 "Level 2 Hint: The correct is not Birdae.\n",
                 "Level 3 Hint: The correct answers are not Birdae and Laridae\n"]
        character = {"X-coordinate": 4, "Y-coordinate": 2, "Current HP": 5, "Level": 1, "XP": 0}
        actual = verify_trivia_response(response, topic, character)
        self.assertEqual(expected, actual)

    def test_verify_trivia_response_correct_input_very_hard_level(self):
        expected = {"X-coordinate": 4, "Y-coordinate": 3, "Current HP": 5, "Level": 1, "XP": 1}
        response = 'B'
        topic = [['b', 'B'],
                 (
                     "Le Sserafim is a (formerly six) five-member K-pop girl group under Source Music, "
                     "a subsidiary of which entertainment company?\n"
                     "a. JYP Entertainment\n"
                     "b. HYBE Corporation\n"
                     "c. SM Entertainment\n"
                     "d. YG Entertainment\n"
                 ),
                 "Level 2 Hint: Le Sserafim is not associated with JYP Entertainment (a is incorrect).\n",
                 "Level 3 Hint: Le Sserafim is not associated with JYP Entertainment nor SM Entertainment (a "
                 "and c are incorrect).\n"]
        character = {"X-coordinate": 4, "Y-coordinate": 3, "Current HP": 5, "Level": 1, "XP": 0}
        actual = verify_trivia_response(response, topic, character)
        self.assertEqual(expected, actual)

    def test_verify_trivia_response_incorrect_input_very_hard_level(self):
        expected = {"X-coordinate": 4, "Y-coordinate": 3, "Current HP": 4, "Level": 1, "XP": 0}
        response = 'a'
        topic = [['b', 'B'],
                 (
                     "Le Sserafim is a (formerly six) five-member K-pop girl group under Source Music, "
                     "a subsidiary of which entertainment company?\n"
                     "a. JYP Entertainment\n"
                     "b. HYBE Corporation\n"
                     "c. SM Entertainment\n"
                     "d. YG Entertainment\n"
                 ),
                 "Level 2 Hint: Le Sserafim is not associated with JYP Entertainment (a is incorrect).\n",
                 "Level 3 Hint: Le Sserafim is not associated with JYP Entertainment nor SM Entertainment (a "
                 "and c are incorrect).\n"]
        character = {"X-coordinate": 4, "Y-coordinate": 3, "Current HP": 5, "Level": 1, "XP": 0}
        actual = verify_trivia_response(response, topic, character)
        self.assertEqual(expected, actual)

    def test_verify_trivia_response_correct_input_final_boss_level(self):
        expected = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5, "Level": 3, "XP": 1}
        response = '4'
        topic = ['4',
                 "Final Boss question: How many times have I been included in the BC/YK provincial team in figure "
                 "skating?\n Enter an integer (if you don’t know the answer, enter your best integer guess).\n",
                 "Level 2 Hint: The number is between 1 and 5 inclusive.\n",
                 "Level 3 Hint: The number is between 2 and 4 inclusive.\n"]
        character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5, "Level": 3, "XP": 0}
        actual = verify_trivia_response(response, topic, character)
        self.assertEqual(expected, actual)

    def test_verify_trivia_response_incorrect_input_final_boss_level(self):
        expected = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 4, "Level": 3, "XP": 0}
        response = '2'
        topic = ['4',
                 "Final Boss question: How many times have I been included in the BC/YK provincial team in figure "
                 "skating?\n Enter an integer (if you don’t know the answer, enter your best integer guess).\n",
                 "Level 2 Hint: The number is between 1 and 5 inclusive.\n",
                 "Level 3 Hint: The number is between 2 and 4 inclusive.\n"]
        character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5, "Level": 3, "XP": 0}
        actual = verify_trivia_response(response, topic, character)
        self.assertEqual(expected, actual)

    def test_verify_trivia_response_incorrect_input_blank_input(self):
        expected = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 4, "Level": 3, "XP": 0}
        response = ''
        topic = ['4',
                 "Final Boss question: How many times have I been included in the BC/YK provincial team in figure "
                 "skating?\n Enter an integer (if you don’t know the answer, enter your best integer guess).\n",
                 "Level 2 Hint: The number is between 1 and 5 inclusive.\n",
                 "Level 3 Hint: The number is between 2 and 4 inclusive.\n"]
        character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5, "Level": 3, "XP": 0}
        actual = verify_trivia_response(response, topic, character)
        self.assertEqual(expected, actual)
