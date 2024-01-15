import unittest
canUnlockAll = __import__('0-lockboxes').canUnlockAll


class TestLockBoxes(unittest.TestCase):
    def test_canUnlockAll_positive_cases(self):
        boxes1 = [[1], [2], [3], [4], []]
        self.assertTrue(canUnlockAll(boxes1),
                        "❌ test_canUnlockAll_positive_cases All boxes can be unlocked.")
        print("test_canUnlockAll_positive_cases 0 ✅")
        boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        self.assertTrue(canUnlockAll(boxes2),
                        "❌ Test passed: All boxes can be unlocked.")
        print("test_canUnlockAll_positive_cases 1 ✅")

    def test_canUnlockAll_negative_cases(self):
        boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        self.assertFalse(canUnlockAll(boxes3),
                         "❌ test_canUnlockAll_negative_cases: Not all boxes can be unlocked.")
        print("test_canUnlockAll_negative_cases 0 ✅")
        boxes4 = [[]]
        self.assertFalse(canUnlockAll(boxes4),
                         "❌ test_canUnlockAll_negative_cases: Not all boxes can be unlocked.")
        print("test_canUnlockAll_negative_cases 1 ✅")

    def test_canUnlockAll_empty_input(self):
        boxes5 = []
        self.assertFalse(canUnlockAll(boxes5),
                         "❌ test_canUnlockAll_empty_input: Not all boxes can be unlocked.")
        print("test_canUnlockAll_empty_input 1 ✅")

    def test_canUnlockAll_single_box(self):
        boxes6 = [[]]
        self.assertFalse(canUnlockAll(boxes6),
                        "❌ test_canUnlockAll_single_box: All boxes can be unlocked.")
        print("test_canUnlockAll_single_box 0 ✅")

    def test_canUnlockAll_no_starting_keys(self):
        boxes7 = [[1, 2], [3], [4], [5], [6]]
        self.assertTrue(canUnlockAll(boxes7),
                         "❌ test_canUnlockAll_no_starting_keys: Not all boxes can be unlocked.")
        print("test_canUnlockAll_no_starting_keys 0 ✅")


if __name__ == '__main__':
    unittest.main()
