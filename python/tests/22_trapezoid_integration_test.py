import pytest

from numeric.trapezoid_integration import trapezoid

def test_trapezoid_integration():
    step = 5
    values = [0, 1.5297, 9.5120, 8.7025, 2.8087, 1.0881, 0.3537]
    
    ans = trapezoid(values, step)
    assert pytest.approx(119, 0.1) == ans