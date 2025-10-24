#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculates the factorial of a given non-negative integer using recursion.
        The factorial of a number n is the product of all positive integers less than or equal to n.
        Mathematically, factorial(n) = n × (n-1) × (n-2) × ... × 1, and factorial(0) = 1.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial value of the given number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the integer argument from the command line
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)
