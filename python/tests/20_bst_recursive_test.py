import pytest

from data_structures.bst_recursive import *

def test_init():
    bst = BinarySearchTree()
    assert bst.size == 0

def test_insert():
    bst = BinarySearchTree()
    nodes = [(15,2), (10,1), (20,7), (3,45), (13,12)]
    
    for k, v in nodes:
        bst.insert(k, v)

    assert bst.size == 5
    assert bst.inorder() == [(3,45), (10,1), (13,12), (15,2), (20,7)]

def test_search():
    bst = BinarySearchTree()
    nodes = [(15,2), (10,1), (20,7), (3,45), (13,12)]
    
    for k, v in nodes:
        bst.insert(k, v)

    for k, v in nodes:
        assert bst.search(k) == v