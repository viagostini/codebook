"""
Number is represented as array of digits in reverse order
For example, to represent 167318 = [8, 1, 3, 7, 6, 1]

For now, we handle only positive numbers
"""

# converts string to big integer array format
def to_number(string):
    a = []
    for c in reversed(string):
        a.append(int(c))
    return a

# converts big integer to string format
def to_string(number):
    a = ''
    for c in reversed(number):
        a += str(c)
    return a

# return c = a + b
def add(a, b):
    # force len(a) >= len(b)
    if len(a) < len(b):
        a, b = b, a
    
    # pad smaller number with zeroes
    len_diff = len(a) - len(b)
    b.extend([0] * len_diff)

    # perform sum
    carry = 0
    c = [0] * len(a)
    for i in range(len(a)):
        c[i] = a[i] + b[i] + carry
        
        if c[i] > 9:
            carry = 1
            c[i]  -= 10

    if carry:
        c.append(carry)

    return c

def subtract(a, b):
    pass