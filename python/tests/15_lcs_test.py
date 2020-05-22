import pytest

from strings.lcs import *

def test_lcs():
    assert lcs('abcdef', 'abfde') == 'abde'
    assert lcs('anothertest', 'notatest') == 'nottest'
    assert lcs('abcd', 'efgh') == ''