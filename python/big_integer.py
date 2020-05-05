"""
Number is represented as an array of digits in reverse order
appended by positive or minus sign

For example, -167318 = [8, 1, 3, 7, 6, 1, '-']
             +167318 = [8, 1, 3, 7, 6, 1, '+']
"""

# converts string to big integer array format
def to_number(s):
    a = [int(c) for c in reversed(s[1:])]
    a.append(s[0])
    return a

# converts big integer to string format
def to_string(number):
    return number[-1] + ''.join([str(c) for c in reversed(number[:-1])])

# returns c = a + b, handles sign
def add(a, b):
    if a[-1] == b[-1]:
        c = _add(a[:-1], b[:-1]) + [a[-1]]
    
    else:
        if greater_than(absolute(a), absolute(b)):
            c = _subtract(a[:-1], b[:-1]) + [a[-1]]
        else:
            c = _subtract(b[:-1], a[:-1]) + [b[-1]]
    
    # avoids -0 problem
    if to_string(c) == '-0':
        c[-1] = '+'
    
    return c

# returns abs(a)
def absolute(a):
    b = a.copy()
    b[-1] = '+'
    return b

# note: -0 != +0
def equals(a, b):
    return to_string(a) == to_string(b)

# returns True if a > b, False otherwise
# note: remember that we can have +0 and -0
def greater_than(a, b):
    if a[-1] != b[-1]:
        return True if a[-1] == '+' else False
    
    if len(a) == len(b):
        return to_string(a) > to_string(b)

    return True if len(a) > len(b) else False

# return c = a + b for a, b >= 0, without sign in array
def _add(a, b):
    # force len(a) >= len(b) since a, b >= 0
    if len(a) < len(b):
        a, b = b, a
    
    # pad smaller number with zeroes
    b.extend([0] * (len(a) - len(b)))

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

def minus(a):
    b = a.copy()
    b[-1] = '+' if b[-1] == '-' else '-'
    return b

# return c = a - b for a >= b
def _subtract(a, b):
    if len(a) >= len(b):
        b.extend([0] * (len(a) - len(b)))
    else:
        a.extend([0] * (len(a) - len(b)))

    c = [0] * len(a)
    for i in range(len(a)):
        if a[i] < b[i]:
            a[i] += 10
            a[i+1] -= 1
        c[i] = a[i] - b[i]
    
    # remove trailing zeroes except possibly one (to represent 0)
    while c[-1] == 0 and len(c) > 1:
        del c[-1]

    return c

# return a - b = a + (-b)
def subtract(a,b):
    b[-1] = '+' if b[-1] == '-' else '-'
    return add(a,b)