"""
Computes gcd(a,b) for a >= 0, b >= 0

Time Complexity: O(log min(a,b))
Space Complexity: O(1)
"""
def gcd(a, b):
    while b > 0:
        a = a % b
        a, b = b, a
    
    return a

"""
Computes gcd(a,b) for a >= 0, b >= 0

Time Complexity: O(log min(a,b))
Space Complexity: O(log min(a,b)) recursion calls
"""
def gcd_r(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

"""
Computes gcd(a, b) and x, y such that
    a * x + b * y = gcd(a,b)

Time Complexity: O(log min(a,b))
Space Complexity: O(log min(a,b)) recursion calls
"""
def xgcd(a, b):
    if a == 0:
        return (b, 0, 1)
    
    g, y, x = xgcd(b % a, a)
    return (g, x - (b // a) * y, y)

"""
Computes lcm(a,b) for a >= 0, b >= 0

Time Complexity: O(log min(a,b))
Space Complexity: O(1)
"""
def lcm(a, b):
    return a * b / gcd(a, b)