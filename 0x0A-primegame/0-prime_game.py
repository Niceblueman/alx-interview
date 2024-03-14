#!/usr/bin/python3
""" 0-prime_game.py """


def is_prime(num):
    """ check for prime number"""
    if num == 0 or num == 1 or (num % 2 == 0 and num > 2):
        return False
    else:
        for i in range(3, int(num ** 0.5) + 2):
            if num % i == 0:
                return False
        return True


def is_round_winner(n, x):
    """ checks the round winner """
    list = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        current_player = players[i % 2]
        nums_selected = []
        prime = -1
        for idx, num in enumerate(list):
            if prime != -1:
                if num % prime == 0:
                    nums_selected.append(idx)
            else:
                if is_prime(num):
                    nums_selected.append(idx)
                    prime = num

        if prime == -1:
            if current_player == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for i, val in enumerate(nums_selected):
                del list[val - i]
    return None


def isWinner(x, nums):
    """ returns the winner """
    counter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        round_winner = is_round_winner(nums[i], x)
        if round_winner is not None:
            counter[round_winner] += 1

    if counter['Maria'] > counter['Ben']:
        return 'Maria'
    elif counter['Ben'] > counter['Maria']:
        return 'Ben'
    else:
        return None
