#!/usr/bin/python3
"""
utf-8 validation function
"""


def validUTF8(bytes):
    """validate supposed utf8 data
    Args:
        bytes (list[int]): _description_
    Returns:
        bool: if Valid utf8
    """
    def char_length(bytes):
        char_count = 0
        i = 0

        while i < len(bytes):
            char_count += 1
            if bytes[i] & 0b10000000 == 0b00000000:
                i += 1
                continue
            elif bytes[i] & 0b11100000 == 0b11000000:
                expected_len = 2
            elif bytes[i] & 0b11110000 == 0b11100000:
                expected_len = 3
            elif bytes[i] & 0b11111000 == 0b11110000:
                expected_len = 4
            else:
                return -1
            while expected_len > 1:
                i += 1
                if i >= len(bytes):
                    return -1
                if bytes[i] & 0b11000000 != 0b10000000:
                    return -1
                expected_len -= 1

            i += 1
        return char_count
    return char_length(bytes) != -1
