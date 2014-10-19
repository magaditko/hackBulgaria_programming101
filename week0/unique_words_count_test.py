import unittest

from unique_words_count import unique_words_count


class UniqueWordsTest(unittest.TestCase):

    def test_count_when_array_is_empty(self):
        self.assertEqual(0, unique_words_count([]))

    def test_count_for_the_correct_count(self):
        self.assertEqual(1, unique_words_count(['tomato']))

    def test_count_for_empty_string_in_array(self):
        self.assertEqual(0, unique_words_count(['', ' ']))

if __name__ == "__main__":
    unittest.main()
