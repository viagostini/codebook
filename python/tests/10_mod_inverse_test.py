import pytest
from mod_inverse import *

def test_mod_inverse():
    assert modinv(7919, 326) == 151
    assert modinv(329377, 121802) == 88685