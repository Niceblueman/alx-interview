#!/usr/bin/python3
"""
Solves the lock boxes puzzle with a more detailed implementation.
"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.

    Args:
        boxes (list): List containing all the boxes with the keys.

    Returns:
        bool: True if all boxes can be opened, otherwise, False.
    """
    if not boxes or not boxes[0]:
        return False

    num_boxes = len(boxes)
    unlocked_boxes = set([0])
    keys_to_check = boxes[0]

    while keys_to_check:
        key = keys_to_check.pop(0)

        if key < num_boxes and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            keys_to_check.extend(boxes[key])

    return len(unlocked_boxes) == num_boxes
