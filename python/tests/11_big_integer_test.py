import pytest
from big_integer import *

def test_convert_to_number():
    assert to_number("23782") == [2, 8, 7, 3, 2]

def test_convert_to_string():
    assert to_string([2, 8, 7, 3, 2]) == "23782"

def test_add():
    a = [4, 1]
    b = [2, 4, 9, 2]
    assert add(a, b) == [6, 5, 9, 2]
    a = [4, 1, 1, 9]
    b = [2, 4, 9, 2]
    assert add(a, b) == [6, 5, 0, 2, 1]