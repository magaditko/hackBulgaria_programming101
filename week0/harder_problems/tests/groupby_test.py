import unittest

import sys
sys.path.insert(0, '../')

from groupby import groupby


class GroupByTest(unittest.TestCase):

    def test_if_sequence_is_empty(self):
        self.assertEqual({}, groupby(lambda x: x % 2, []))

    def test_should_return_correct_result(self):
        function = groupby(lambda x: 'even' if x % 2 else 'odd', [1, 2, 3, 5])
        self.assertEqual({'odd': [2], 'even': [1, 3, 5]}, function)

    def test_should_not_return_empty_dictionary(self):
        function = groupby(lambda x: x % 3, [0, 1, 2, 3, 4])
        self.assertNotEqual({}, function)

if __name__ == "__main__":
    unittest.main()
