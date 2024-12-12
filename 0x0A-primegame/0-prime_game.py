#!/usr/bin/python3
"""Prime game"""


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if not nums or x <= 0:
        return None

    # Find the maximum n value in nums to limit the sieve
    max_n = max(nums)

    # Sieve of Eratosthenes to determine primes up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Precompute the number of primes up to each number n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # If the number of primes up to n is odd, Maria wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
