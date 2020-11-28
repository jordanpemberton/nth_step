"""
Jordan Pemberton
CS325 Algorithms
Extra Credit: Nth Step Problem
"""


from math import factorial as fct


def nth_step_math(n, m=2):
    """
    Using permutations formula, factorial
    to solve nth step problem.
    **Only works for 1 or 2 step version (m=2).
    """
    total = 0
    for k in range(n//2+1):
        total +=  fct(n-k) / ( fct(n-2*k) * fct(k))
    return total


if __name__ == '__main__':
    # m = 3       # doesn't work
    m = 2
    for i in range(10):
        print(i, nth_step_math(i, m))
