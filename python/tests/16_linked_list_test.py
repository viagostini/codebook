import pytest
from linked_list import *

def test_initialization():
    L = LinkedList()
    assert L.size == 0
    assert L.head == None

def test_insert():
    L = LinkedList()
    
    L.insert(7)
    assert L.size == 1
    assert L.to_list() == [7]

    L.insert(2)
    assert L.size == 2
    assert L.to_list() == [7, 2]
    
    L.insert(12, 1)
    assert L.size == 3
    assert L.to_list() == [7, 12, 2]

def test_delete():
    L = LinkedList()
    
    L.insert(7)
    L.insert(12)
    L.insert(5)
    L.insert(2)

    L.delete()
    assert L.to_list() == [7, 12, 5]
    
    L.delete(1)
    assert L.to_list() == [7, 5]
    
    L.delete(1)
    assert L.to_list() == [7]
    
    L.delete()
    assert L.to_list() == []

def test_get():
    L = LinkedList()
    assert L.get(0) == None

    L.insert(12)
    L.insert(2)
    L.insert(7, 0)
    
    assert L.get(0) == 7
    assert L.get(1) == 12
    assert L.get(2) == 2