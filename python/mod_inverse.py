from euclides import *

"""
Computes a^(-1) mod m
Assumes gcd(a, m) = 1

Time Complexity: O(log min(a,b))
Space Complexity: O(log min(a,b)) recursion calls
"""
def modinv(a, m):
    g, x, y = xgcd(a, m)
    return x % m