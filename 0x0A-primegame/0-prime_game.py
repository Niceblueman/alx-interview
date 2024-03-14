#!/usr/bin/python3
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        primes = get_primes(n)
        total_primes = len(primes)
        if total_primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins == ben_wins:
        return None
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return "Ben"
