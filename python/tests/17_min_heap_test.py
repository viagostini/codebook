import pytest

from data_structures.min_heap import *

def test_init():
    h = MinHeap()
    assert h.heap == [0]

def test_build_heap():
    h = MinHeap()
    h.build_heap([9, 6, 5, 2, 3])
    assert h.heap == [0, 2, 3, 5, 6, 9]

def test_insert():
    h = MinHeap()
    h.insert(1)
    assert h.heap == [0, 1]
    h.insert(3)
    assert h.heap == [0, 1, 3]
    h.insert(-2)
    assert h.heap == [0, -2, 3, 1]

def test_max():
    h = MinHeap()
    assert h.min_element() == None
    h.insert(1)
    assert h.min_element() == 1
    h.insert(3)
    assert h.min_element() == 1
    h.insert(-2)
    assert h.min_element() == -2

def test_extract_min():
    h = MinHeap()
    h.insert(1)
    h.insert(3)
    h.insert(-2)
    assert h.extract_min() == -2
    assert h.extract_min() == 1
    assert h.extract_min() == 3
    h.insert((2, 1028))
    h.insert((42, 25))
    assert h.extract_min() == (2, 1028)
