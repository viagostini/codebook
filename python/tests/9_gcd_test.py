import pytest
from euclides import *

def test_gcd():
    assert gcd(7919, 326) == 1
    assert gcd(223894,122386) == 22

def test_gcd_recursive():
    assert gcd_r(7919, 326) == 1
    assert gcd_r(223894,122386) == 22

def test_lcm():
    assert lcm(7919, 326) == 2581594
    assert lcm(223894,122386) == 1245522322

def test_extended_gcd():
    assert xgcd(7919, 326) == (1, 151, -3668)
    assert xgcd(223894,122386) == (22, -1911, 3496)