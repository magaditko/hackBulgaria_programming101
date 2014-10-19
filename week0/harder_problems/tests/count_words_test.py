import unittest

import sys
sys.path.insert(0, '../')

import sys
sys.path.insert(0, '../')

from count_words import count_words


class CountWordsTest(unittest.TestCase):

    def test_count_when_array_is_empty(self):
        function = count_words([])
        self.assertEqual({}, function)

    def test_count_for_correct_answer(self):
        function = count_words(['tomato'])
        self.assertEqual({'tomato': 1}, function)

    def test_count_for_incorrect_answer(self):
        function = count_words(['coffee', 'tomato', 'word'])
        self.assertNotEqual({}, function)

    def test_count_for_empty_string_in_array(self):
        function = count_words(['', ' '])
        self.assertEqual({}, function)


if __name__ == "__main__":
    unittest.main()
