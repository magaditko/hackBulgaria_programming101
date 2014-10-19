import unittest

from is_an_bn import is_an_bn


class IsAnBnTest(unittest.TestCase):

    def test_if_word_is_empty(self):
        result = is_an_bn("")
        self.assertTrue(result)

    def test_if_the_answer_should_be_True(self):
        result = is_an_bn("aaabbb")
        self.assertTrue(result)

    def test_if_the_answer_should_be_False(self):
        result = is_an_bn("aabbb")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
