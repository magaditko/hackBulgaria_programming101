import unittest

from groupby import groupby


class GroupByTest(unittest.TestCase):

    def test_if_sequence_is_empty(self):
        self.assertEqual({}, groupby(lambda x: x % 2, []))

if __name__ == "__main__":
    unittest.main()
9
