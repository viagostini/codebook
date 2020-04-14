import pytest
from connected_component import *

@pytest.fixture
def single():
    return {
        0: set([1, 2]),
        1: set([0, 3, 4]),
        2: set([0, 5, 6]),
        3: set([1]),
        4: set([1]),
        5: set([2]),
        6: set([2])
    }

@pytest.fixture
def two_comp():
    return {
        0: set([1, 2]),
        1: set([0]),
        2: set([0]),
        3: set([4]),
        4: set([3])
    }

@pytest.fixture
def isolated():
    return {
        0: set(),
        1: set(),
        2: set()
    }

def test_all_components_single(single):
    ans = [ set([0, 1, 2, 3, 4, 5, 6]) ]
    assert connected_components(single) == ans

def test_all_components_two(two_comp):
    ans = [ set([0, 1, 2]), set([3,4]) ]
    assert connected_components(two_comp) == ans

def test_all_components_isolated(isolated):
    ans = [ set([0]), set([1]), set([2]) ]
    assert connected_components(isolated) == ans