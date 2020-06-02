import pytest

def trapezoid(values, step):
    ans = 0.5 * (values[0] + values[-1])

    for value in values[:-1]:
        ans += value
    
    return step * ans
