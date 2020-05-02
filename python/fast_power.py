"""
Computes x^n for n >= 0.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
def fast_pow(x, n):
    power = 1
    
    while n > 0:
        if n % 2 == 1:
            power = power * x
        x = x ** 2
        n = n // 2
    
    return power

def mod_pow(x, n, mod):
    power, x = 1, x % mod

    while n > 0:
        if n % 2 == 1:
            power = power * x % mod
        x = x ** 2 % mod
        n = n // 2

    return power