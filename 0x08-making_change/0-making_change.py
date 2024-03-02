#!/usr/bin/python3

"""anything here"""


def makeChange(coins, total):
    """_summary_

    Args:
        coins (_type_): _description_
        total (_type_): _description_

    Returns:
        _type_: _description_
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
