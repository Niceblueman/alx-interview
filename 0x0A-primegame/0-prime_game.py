#!/usr/bin/python3
def isWinner(x, nums):
    max_num = 10000
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False
    primes = [num for num in range(2, max_num + 1) if primes[num]]

    def play_game(n):
        numbers = set(range(1, n + 1))
        maria_turn = True
        while True:
            prime_subset = [num for num in numbers if num in primes]
            if not prime_subset:
                return not maria_turn
            if maria_turn:
                maria_choice = min(prime_subset)
                numbers.remove(maria_choice)
                for multiple in range(maria_choice * 2, n + 1, maria_choice):
                    numbers.discard(multiple)
            else:
                ben_choice = min(prime_subset)
                numbers.remove(ben_choice)
                for multiple in range(ben_choice * 2, n + 1, ben_choice):
                    numbers.discard(multiple)
            maria_turn = not maria_turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None