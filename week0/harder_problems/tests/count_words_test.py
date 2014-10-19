import unittest

from count_words import count_words


class CountWordsTest(unittest.TestCase):

    def test_count_when_array_is_empty(self):
        self.assertEqual({}, count_words([]))

    def test_count_if_item_is_not_in_array(self):
        self.assertNotIn("tomato", count_words(["one", "one", "two", "three"]))

    def test_count_if_item_is_in_array(self):
        self.assertIn("tomato", count_words(["one", "tomato", "two", "three"]))

    def test_count_for_the_correct_count(self):
        self.assertEqual({'tomato': 1}, count_words(['tomato']))

    def test_count_for_empty_string_in_array(self):
        self.assertEqual({}, count_words(['', ' ']))


if __name__ == "__main__":
    unittest.main()
