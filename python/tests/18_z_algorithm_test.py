import pytest

from z_algorithm import *

def test_find_all_occurrences():
    s = 'aabcaabxaaaz'
    p = 'aa'
    assert find_all_occurrences(p, s) == [0, 4, 8, 9]

    s = 'aabcaabxaaaz'
    p = 'aab'
    assert find_all_occurrences(p, s) == [0, 4]

    s = 'aabcaabxaaaz'
    p = 'xab'
    assert find_all_occurrences(p, s) == []