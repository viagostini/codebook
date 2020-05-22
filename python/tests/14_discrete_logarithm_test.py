import pytest
from number_theory.discrete_logarithm import *

def test_discrete_logarithm():
    x = discrete_logarithm(5, 7, 17)
    assert pow(5, x, 17) == 7
    
    x = discrete_logarithm(3, 13, 17)
    assert pow(3, x, 17) == 13

    x = discrete_logarithm(2, 4, 7)
    assert pow(2, x, 7) == 4