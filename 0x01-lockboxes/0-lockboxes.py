#!/usr/bin/python3
""" lock boxes puzzle """


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List which contains all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    opened_boxes = {0: {'status': 'opened', 'keys': boxes[0]}}

    while True:
        keys = None
        for index, box in opened_boxes.items():
            if box.get('status') == 'opened':
                box['status'] = 'opened/checked'
                keys = box.get('keys')
                break

        if keys:
            for key in keys:
                try:
                    if opened_boxes.get(key) and opened_boxes.get(key).get('status') == 'opened/checked':
                        continue
                    opened_boxes[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in opened_boxes.values()]:
            continue
        elif len(opened_boxes) == len(boxes):
            break
        else:
            return False

    return len(opened_boxes) == len(boxes)
