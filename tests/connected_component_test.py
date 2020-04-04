import pytest
from connected_component import *

@pytest.fixture
def single():
    return [set([1, 2]), set([0, 3, 4]), set([0, 5, 6]),
             set([1]), set([1]), set([2]), set([2])]

@pytest.fixture
def two_comp():
    return [set([1, 2]), set([0]), set([0]), set([4]), set([3])]

@pytest.fixture
def isolated():
    return [set(), set(), set()]

# ----------- Test Connected Component Method ----------- #

def test_connected_component_single(single):
    ans = set([0, 1, 2, 3, 4, 5, 6])
    for i in range(7):
        assert connected_component(single, i) == ans, "Iteration {}".format(i)

def test_connected_component_two(two_comp):
    comp1 = set([0, 1, 2])
    for i in range(3):
        assert connected_component(two_comp, i) == comp1
    comp2 = set([3, 4])
    for i in range(3, 5):
        assert connected_component(two_comp, i) == comp2

def test_connected_component_isolated(isolated):
    for i in range(3):
        assert connected_component(isolated, i) == set([i])

# ----------- Test All Connected Components Method ----------- #

def test_all_components_single(single):
    ans = [ set([0, 1, 2, 3, 4, 5, 6]) ]
    assert get_all_components(single) == ans

def test_all_components_two(two_comp):
    ans = [ set([0, 1, 2]), set([3,4]) ]
    assert get_all_components(two_comp) == ans

def test_all_components_isolated(isolated):
    ans = [ set([0]), set([1]), set([2]) ]
    assert get_all_components(isolated) == ans