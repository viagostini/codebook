import pytest
from bit_manipulation.bit_manipulation import *

def test_is_set():
    assert is_set(8, 0) == False
    assert is_set(8, 1) == False
    assert is_set(8, 2) == False
    assert is_set(8, 3) == True    

def test_set():
    assert set(8, 0) == 9
    assert set(8, 4) == 24

def test_clear():
    assert clear(8, 3) == 0
    assert clear(2, 1) == 0

def test_toggle():
    assert toggle(8, 3) == 0
    assert toggle(8, 0) == 9

def count():
    assert count(8) == 1
    assert count(12) == 2

def test_hamming_distance():
    assert hamming_distance(8, 2) == 2
    assert hamming_distance(12, 2) == 3

def test_find_unique_element():
    assert find_unique_element([2, 4, 3, 6, 4, 2, 3]) == 6
    assert find_unique_element([75, 37, 22, 18, 75, 18, 22]) == 37