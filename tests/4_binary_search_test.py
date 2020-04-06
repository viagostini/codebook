import pytest
from binary_search import *

@pytest.fixture
def arr():
    return [2, 7, 12, 20, 42, 57] 

# --------- Standard Binary Search Tests --------- #

def test_binary_search_first(arr):
    assert binary_search(arr, 2) == 0
    assert binary_search_recursive(arr, 2) == 0

def test_binary_search_mid(arr):
    assert binary_search(arr, 20) == 3
    assert binary_search_recursive(arr, 20) == 3

def test_binary_search_end(arr):
    assert binary_search(arr, 57) == 5
    assert binary_search_recursive(arr, 57) == 5

def test_binary_search_smaller_than_first(arr):
    assert binary_search(arr, -3) == -1
    assert binary_search_recursive(arr, -3) == -1

def test_binary_search_greater_than_last(arr):
    assert binary_search(arr, 60) == -1
    assert binary_search_recursive(arr, 60) == -1

# --------- Upper Bound Binary Search Tests --------- #

def test_upper_bound_existing_first(arr):
    assert upper_bound(arr, 2) == 1

def test_upper_bound_existing_mid(arr):
    assert upper_bound(arr, 20) == 4

def test_upper_bound_existing_end(arr):
    assert upper_bound(arr, 57) == 6

def test_upper_bound_smaller_than_first(arr):
    assert upper_bound(arr, -3) == 0

def test_upper_bound_between_middle_a(arr):
    assert upper_bound(arr, 35) == 4

def test_upper_bound_between_middle_b(arr):
    assert upper_bound(arr, 9) == 2

def test_upper_bound_greater_than_last(arr):
    assert upper_bound(arr, 60) == 6

# --------- Lower Bound Binary Search Tests --------- #

def test_lower_bound_existing_first(arr):
    assert lower_bound(arr, 2) == 0

def test_lower_bound_existing_mid(arr):
    assert lower_bound(arr, 20) == 3

def test_lower_bound_existing_end(arr):
    assert lower_bound(arr, 57) == 5

def test_lower_bound_smaller_than_first(arr):
    assert lower_bound(arr, -3) == 0

def test_lower_bound_between_middle_a(arr):
    assert lower_bound(arr, 35) == 4

def test_lower_bound_between_middle_b(arr):
    assert lower_bound(arr, 9) == 2

def test_lower_bound_greater_than_last(arr):
    assert lower_bound(arr, 60) == 6
