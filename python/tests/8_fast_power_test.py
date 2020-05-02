import pytest
from fast_power import *

def test_fast_power():
    assert fast_pow(234, 0) == 1
    assert fast_pow(2,17) == 2**17
    assert fast_pow(7, 12) == 7**12
    assert fast_pow(17, 23) == 17**23

def test_mod_power():
    assert mod_pow(234, 0, 17) == 1
    assert mod_pow(2,17, 5) == 2**17 % 5
    assert mod_pow(7, 12, 8) == 7**12 % 3
    assert mod_pow(17, 23, 23) == 17**23 % 23