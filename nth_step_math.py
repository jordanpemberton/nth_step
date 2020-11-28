from math import factorial as fct


def nth_step(n):
    """
    Experimenting, not working yet...
    """
    total = 0
    for k in range(n//2):
        total += (fct(n-k)) / (fct(n-2*k) * fct(k))
 
    return total


if __name__ == '__main__':
    for i in range(10):
        print(i, nth_step(i))
