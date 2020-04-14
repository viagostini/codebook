from floyd_warshall import *

weights = [[0, 9, 1, 30, float('inf')],
        [9, 0, 7, 3, 10],
        [1, 7, 0, 15, float('inf')],
        [30, 3, 15, 0, 8],
        [float('inf'), 10, float('inf'), 8, 0]]

def test_floyd_warshall():
    dists = [[0, 8, 1, 11, 18],
             [8, 0, 7, 3, 10],
             [1, 7, 0, 10, 17],
             [11, 3, 10, 0, 8],
             [18, 10, 17, 8, 0]]

    assert floyd_warshall(weights) == dists