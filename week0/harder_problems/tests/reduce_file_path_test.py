import unittest

import sys
sys.path.insert(0, '../')

from reduce_file_path import reduce_file_path


class ReduceFilePathTest(unittest.TestCase):

    def test_if_path_is_empty(self):
        result = reduce_file_path("")

        self.assertEqual("/", result)

    def test_if_path_is_slash(self):
        result = reduce_file_path("/")

        self.assertEqual("/", result)

    def test_if_path_contains_two_dots(self):
        result = reduce_file_path("/folder/lil/..")

        self.assertEqual("/folder", result)

    def test_if_path_ends_with_slash(self):
        result = reduce_file_path("/folder/another/")

        self.assertEqual("/folder/another", result)

    def test_if_path_contains_one_dot(self):
        result = reduce_file_path("/folder/././")

        self.assertEqual("/folder", result)

    def test_if_path_contains_whitespaces(self):
        result = reduce_file_path(" / folder/.  /")

        self.assertEqual("/folder", result)

    def test_if_path_contains_slashes(self):
        result = reduce_file_path("/ha///lil/")

        self.assertEqual("/ha/lil", result)

if __name__ == "__main__":
    unittest.main()
