#!/usr/bin/python3
"""utf-8 validation function"""


def validUTF8(data):
    """validate supposed utf8 data 

    Args:
        data (list[int]): _description_

    Returns:
        bool: if Valid utf8
    """
    if not data:
        return False
    size = 0
    for char in data:
        if size == 0 and char >> 7 == 0b0:
            continue
        elif size == 0:
            if char >> 5 == 0b110:
                size = 1
            elif char >> 4 == 0b1110:
                size = 2
            elif char >> 3 == 0b11110:
                size = 3
            elif char >> 2 == 0b111110:
                size = 4
            elif char >> 1 == 0b1111110:
                size = 5
            else:
                return False
        else:
            if (char >> 6) != 0b10:
                return False
            size -= 1
    return size == 0
