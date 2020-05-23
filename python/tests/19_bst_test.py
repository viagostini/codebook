import pytest

from data_structures.bst import *

def test_init():
    bst = BinarySearchTree()
    assert bst.size == 0

def test_insert():
    bst = BinarySearchTree()
    nodes = [(15,2), (10,1), (20,7), (3,45), (13,12)]
    
    for k, v in nodes:
        bst[k] = v

    assert bst.size == 5
    assert list(bst) == [(3,45), (10,1), (13,12), (15,2), (20,7)]

def test_search():
    bst = BinarySearchTree()
    nodes = [(15,2), (10,1), (20,7), (3,45), (13,12)]
    
    for k, v in nodes:
        bst[k] = v
    
    for k, _ in nodes:
        assert k in bst

    for k, v in nodes:
        assert bst[k] == v

def test_delete():
    bst = BinarySearchTree()
    nodes = [(15,2), (10,1), (20,7), (3,45), (13,12)]
    
    for k, v in nodes:
        bst[k] = v

    del bst[13]
    assert list(bst) == [(3,45), (10,1), (15,2), (20,7)]

    del bst[10]
    assert list(bst) == [(3,45), (15,2), (20,7)]