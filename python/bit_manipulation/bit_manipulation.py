from functools import reduce

# returns True if i-th bit of x is set, false otherwise
def is_set(x, i):
    return x & (1 << i) != 0

# clears i-th bit of x
def clear(x, i):
    return x & ~(1 << i)

# sets i-th bit of x
def set(x, i):
    return x | (1 << i)

# toggles i-th bit of x
def toggle(x, i):
    return x ^ (1 << i)

# counts number of set bits in x
def count(x):
    count = 0
    
    while x:
        x &= x-1
        count += 1
    
    return count

# calculates hamming distance of x and y (x^y = x XOR y)
def hamming_distance(x, y):    
    return count(x^y)

# returns x such that there is only one occurence of x in arr
def find_unique_element(arr):
    return reduce(lambda x, y: x^y, arr)