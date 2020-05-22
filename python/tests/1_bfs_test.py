import pytest

from graphs.bfs import *

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

def test_bfs_single(single):
    ans = set([0, 1, 2, 3, 4, 5, 6])
    for i in range(7):
        assert bfs(single, i) == ans

def test_bfs_two(two_comp):
    comp1 = set([0, 1, 2])
    for i in range(3):
        assert bfs(two_comp, i) == comp1
    comp2 = set([3, 4])
    for i in range(3, 5):
        assert bfs(two_comp, i) == comp2

def test_bfs_isolated(isolated):
    for i in range(3):
        assert bfs(isolated, i) == set([i])
