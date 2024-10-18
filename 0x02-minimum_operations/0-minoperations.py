#!/usr/bin/python3
"""In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to reach exactly `n` "H"
    characters starting from one "H", using only "Copy All" and "Paste".

    Parameters:
    n (int): The target number of "H" characters.

    Returns:
    int: The minimum number of operations required, or 0 if it's not possible
         to achieve `n` characters.

    The method:
    - Starts with 1 "H".
    - If `n` can be factored into smaller parts, we can reduce the number of
      operations by using "Copy All" and "Paste" strategically based on
      divisors.
    - For each factor, it simulates a "Copy All" followed by multiple "Paste"
        operations.

    Example:
    For n = 9:
        H => Copy All => Paste => HH => Paste => HHH => Copy All =>
        Paste => HHHHHH => Paste => HHHHHHHHH
        (Total operations: 6)

    Edge case:
    - If n <= 1, return 0 (as it's impossible or unnecessary to achieve n).

    Example usage:
    >>> minOperations(4)
    4

    >>> minOperations(12)
    7
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        # Divide n by its smallest divisor and then add divisor to operations
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
