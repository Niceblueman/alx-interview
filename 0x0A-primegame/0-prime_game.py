#!/usr/bin/python3
"""Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
    def remove_prime_multiples(ls, x):
        """removes multiples of primes"""
        for i in range(2, len(ls)):
            try:
                ls[i * x] = 0
            except (ValueError, IndexError):
                break

    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for _ in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    [remove_prime_multiples(a, i) for i in range(2, len(a))]

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None
