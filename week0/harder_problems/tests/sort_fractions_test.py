import unittest

from sort_fractions import sort_fractions


class SortFractionsTest(unittest.TestCase):

    def test_check_if_the_list_is_empty(self):
        result = sort_fractions([])
        self.assertEqual([], result)

    def test_if_fraction_contains_non_integers(self):
        result = sort_fractions([("a", "b"), (1, 2)])
        self.assertEqual([(1, 2)], result)

    def test_should_return_the_right_result(self):
        result = sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)])
        self.assertEqual([(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)], result)

if __name__ == "__main__":
    unittest.main()
