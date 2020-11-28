"""
Jordan Pemberton
CS325 Algorithms
Extra Credit: Nth Step Problem
"""

def nth_step(n, m=2):
    """
    Returns the number of ways to climb n
    stairs, with opts [1..m] steps at a time.
    Uses a dynamic programming, memoization
    method very similar to that used to
    find Fibonacci numbers.
    """
    temp = 0
    memo = {0: 1}
    for i in range(1, n+1):
        if (i > m):
            temp -= memo[i - m - 1]
        temp += memo[i - 1]
        memo[i] = temp
    return memo[n]
