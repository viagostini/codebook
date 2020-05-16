import pytest
from lcs import *

def test_lcs():
    assert lcs('abcdef', 'abfde') == 'abde'
    assert lcs('anothertest', 'notatest') == 'nottest'