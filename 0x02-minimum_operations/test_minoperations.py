import unittest
from importlib import import_module

minOperations = import_module("0-minoperations").minOperations


class TestMinOperations(unittest.TestCase):

    def test_min_operations(self):
        self.assertEqual(minOperations(4), 4, "test_min_operations 0")
        self.assertEqual(minOperations(12), 7, "test_min_operations 1")
        self.assertEqual(minOperations(9), 6, "test_min_operations 2")
        print("\ttest_min_operations: success")
    def test_invalid_input(self):
        self.assertEqual(minOperations(1), 0, "test_invalid_input 0")
        self.assertEqual(minOperations(0), 0, "test_invalid_input 1")
        self.assertEqual(minOperations(-5), 0, "test_invalid_input 2")
        self.assertEqual(minOperations("invalid"), 0, "test_invalid_input 3")
        print("\ttest_invalid_input: success")


if __name__ == '__main__':
    unittest.main()
