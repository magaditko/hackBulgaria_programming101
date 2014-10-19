import unittest

from simplify_fracction import simplify_fraction


class SimplifyFractionTest(unittest.TestCase):

    def test_if_fraction_contains_non_integers(self):
        result = simplify_fraction(("a", "b"))
        self.assertIsNone(result)

    def test_can_be_reduced(self):
        result = simplify_fraction((1, 3))
        self.assertEqual((1, 3), result)

    def test_can_not_be_reduces(self):
        result = simplify_fraction((1, 7))
        self.assertEqual((1, 7), result)

if __name__ == "__main__":
    unittest.main()
