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
    curr = 0
    memo = {0: 1}
    for i in range(1, n+1):
        # If remaining stairs > step size
        if (i > m):
            curr -= memo[i - m - 1]
        curr += memo[i - 1]
        # Save:
        memo[i] = curr
    return memo[n]


if __name__ == '__main__':
    # m = 2
    print('1 or 2 steps allowed, 1 to 10 stairs:')
    for i in range(10):
        print(i + 1, ': ', nth_step(i + 1))

    print()

    # m = 3
    print('1, 2, or 3 steps allowed, 1 to 10 stairs:')
    m = 3
    for i in range(10):
        print(i + 1, ': ', nth_step(i + 1, m))
