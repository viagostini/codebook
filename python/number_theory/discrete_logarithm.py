from math import sqrt, floor

def discrete_logarithm(a, b, m):
    '''
    Returns x such that a^x mod m = b or -1 if there is no solution.
    If there is more than one solution, returns only one of them.
    Assumes gcd(a, m) = 1.

    https://en.wikipedia.org/wiki/Baby-step_giant-step

    Time Complexity: O(sqrt(m))
    Space Complexity: O(sqrt(m))
    '''
    n = floor(sqrt(m)) + 1

    an = 1
    for _ in range(n):
        an = (an * a) % m
    
    table, curr = {}, an
    for p in range(1, n+1):
        table[curr] = p
        curr = (curr * an) % m

    curr = b
    for q in range(n+1):
        if curr in table:
            return table[curr] * n - q
        curr = (curr * a) % m

    return -1