import unittest
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle


class TestPascalTriangle(unittest.TestCase):

    def test_pascal_triangle(self):

        # Test case for n = 0
        print("Test case for n = 0 ✅")
        self.assertEqual(pascal_triangle(0), [])
        print("Test case for n = 1 ✅")
        self.assertEqual(pascal_triangle(1), [
            [1]
        ])
        print("Test case for n = 2 ✅")
        self.assertEqual(pascal_triangle(2), [
            [1],
            [1, 1]
        ])
        print("Test case for n = 3 ✅")
        self.assertEqual(pascal_triangle(3), [
            [1],
            [1, 1],
            [1, 2, 1]
        ])
        print("Test case for n = 4 ✅")
        self.assertEqual(pascal_triangle(4), [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1]
        ])
        print("Test case for n = 5 ✅")
        self.assertEqual(pascal_triangle(5), [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ])
        # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
