from unittest import TestCase

from game import trivia_topics


class Test(TestCase):
    def test_trivia_topics_easy_trivia_in_trivia_list(self):
        provinces = [{'d', 'D'},
                     ("Which Canadian province(s) have I not visited as of November 2024?\n"
                      "a. Quebec\n"
                      "b. Saskatchewan\n"
                      "c. Both a and b\n"
                      "d. None of the above\n"
                      ),
                     "Level 2 Hint: The correct answer is not c.\n",
                     "Level 3 Hint: I have been to Quebec for a national level figure skating competition. In other "
                     "words, the incorrect answers are a and c\n"]
        expected = provinces
        topics_list = trivia_topics()
        easy_list = topics_list[0]
        self.assertTrue(expected in easy_list)

    def test_trivia_topics_medium_trivia_in_trivia_list(self):
        soil = [{'f', 'F'},
                "Choose T (True) or F (False) for the following statement:\nSoil is the same thing as dirt.\n",
                "Level 2 Hint: Think about where you find soil versus dirt.\n",
                "Level 3 Hint: Soil is a natural layer of earth often found with living plants and organisms. Does dirt"
                " have all the same features as soil?\n"]
        expected = soil
        topics_list = trivia_topics()
        medium_list = topics_list[1]
        self.assertTrue(expected in medium_list)

    def test_trivia_topics_hard_trivia_in_trivia_list(self):
        crows = [{'d', 'D'},
                 ("Which family do crows belong to?\n"
                  "a. Coraciiformes\n"
                  "b. Birdae\n"
                  "c. Laridae\n"
                  "d. Corvidae\n"),
                 "Level 2 Hint: The correct is not Birdae.\n",
                 "Level 3 Hint: The correct answers are not Birdae and Laridae\n"]
        expected = crows
        topics_list = trivia_topics()
        hard_list = topics_list[2]
        self.assertTrue(expected in hard_list)

    def test_trivia_topics_very_hard_trivia_in_trivia_list(self):
        le_sserafim = [{'b', 'B'},
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
        expected = le_sserafim
        topics_list = trivia_topics()
        very_hard_list = topics_list[3]
        self.assertTrue(expected in very_hard_list)

    def test_trivia_topics_final_boss_trivia_in_trivia_list(self):
        bc_team = ['4',
                   "Final Boss question: How many times have I been included in the BC/YK provincial team in figure "
                   "skating?\n Enter an integer (if you don’t know the answer, enter your best integer guess).\n",
                   "Level 2 Hint: The number is between 1 and 5 inclusive.\n",
                   "Level 3 Hint: The number is between 2 and 4 inclusive.\n"]
        expected = bc_team
        topics_list = trivia_topics()
        final_boss_list = topics_list[4]
        self.assertTrue(expected in final_boss_list)
