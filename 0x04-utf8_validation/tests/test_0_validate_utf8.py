#!/usr/bin/python3
"""
Unit tests for the validUTF8 function
"""

import unittest
validUTF8 = __import__('0-validate_utf8').validUTF8


class TestUTF8Validation(unittest.TestCase):
    def test_single_byte_character(self):
        data = [65]
        self.assertTrue(validUTF8(data),
                        "Test failed for single-byte character")

    def test_multiple_byte_characters(self):
        data = [80, 121, 116, 104, 111, 110, 32,
                105, 115, 32, 99, 111, 111, 108, 33]
        self.assertTrue(validUTF8(data),
                        "Test failed for multiple-byte characters")

    def test_invalid_encoding(self):
        data = [229, 65, 127, 256]
        self.assertFalse(validUTF8(data), "Test failed for invalid encoding")


if __name__ == '__main__':
    unittest.main()
