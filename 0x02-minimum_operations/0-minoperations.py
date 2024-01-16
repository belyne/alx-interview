#!/usr/bin/python3
"""
Calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations needed.
        If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    operations = 0
    i = 2

    while i <= n:
        if n % i == 0:
            n //= i
            operations += i
        else:
            i += 1

    return operations
