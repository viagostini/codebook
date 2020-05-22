import pytest
from geometry.polygon import *

def test_ccw():
    assert ccw((3,2), (2,3), (1,2)) > 0
    assert ccw((1,2), (2,3), (3,2)) < 0
    assert ccw((1,1), (2,2), (3,3)) == 0

def test_is_convex():
    points = [(0,0), (5, 0), (5, 5), (0, 5)]
    assert is_convex(points) == True

    points = [(-3,-2), (-1,4), (6,1), (3,10), (-4,9)]
    assert is_convex(points) == False

def test_area():
    points = [(0,0), (5, 0), (5, 5), (0, 5)]
    assert area(points) == 25

    points = [(-4,3), (5,1), (2, 5)]
    assert area(points) == 15

    points = [(-3,-2), (-1,4), (6,1), (3,10), (-4,9)]
    assert area(points) == 60