import pytest
from big_integer import *

def test_convert_to_number():
    assert to_number('+23782') == [2, 8, 7, 3, 2, '+']
    assert to_number('-23782') == [2, 8, 7, 3, 2, '-']

def test_convert_to_string():
    assert to_string([2, 8, 7, 3, 2, '+']) == '+23782'
    assert to_string([2, 8, 7, 3, 2, '-']) == '-23782'

def test_add():
    # same sign
    a, b = [4, 1, '+'], [2, 4, 9, 2, '+']
    c, d = [4, 1, '-'], [2, 4, 9, 2, '-']

    assert add(a, b) == [6, 5, 9, 2, '+']
    assert add(c, d) == [6, 5, 9, 2, '-']

    # different signs
    a, b = [5, 3, 2, '+'], [0, 0, 2, '-'] # contains trailing zeroes
    c, d = [2, 4, 9, 2, '+'], [4, 1, 1, 9, '-']

    assert add(a, b) == [5, 3, '+']
    assert add(c, d) == [2, 7, 1, 6, '-']

    # -0 test
    a, b = [2, 4, 9, 2, '+'], [2, 4, 9, 2, '-']
    assert add(a, b) == [0, '+']

def test_subtract():
    # same sign
    a, b = [4, 1, '+'], [2, 4, 9, 2, '+']
    c, d = [4, 1, '-'], [2, 4, 9, 2, '-']

    assert subtract(a, b) == [8, 2, 9, 2, '-']
    assert subtract(c, d) == [8, 2, 9, 2, '+']

    # different signs
    a, b = [5, 3, 2, '-'], [0, 0, 2, '+'] # contains trailing zeroes
    c, d = [2, 4, 9, 2, '+'], [4, 1, 1, 9, '-']

    assert subtract(a, b) == [5, 3, 4, '-']
    assert subtract(c, d) == [6, 5, 0, 2, 1, '+']