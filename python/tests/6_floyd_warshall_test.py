from graphs.floyd_warshall import *

weights = [[0, 9, 1, 30, float('inf')],
        [9, 0, 7, 3, 10],
        [1, 7, 0, 15, float('inf')],
        [30, 3, 15, 0, 8],
        [float('inf'), 10, float('inf'), 8, 0]]

missing_paths = [[0, 3, 2, float('inf')],
                 [float('inf'), 0, float('inf'), float('inf')],
                 [float('inf'), float('inf'), 0, 1],
                 [float('inf'), 5, 1, float('inf')]]

negative = [[0, 7, 5],
            [7, 0, -3],
            [5, float('inf'), 0]]

def test_floyd_warshall():
    dists = [[0, 8, 1, 11, 18],
             [8, 0, 7, 3, 10],
             [1, 7, 0, 10, 17],
             [11, 3, 10, 0, 8],
             [18, 10, 17, 8, 0]]

    preds = [[0, 2, 2, 2, 2],
             [2, 1, 2, 3, 4],
             [0, 1, 2, 1, 1],
             [1, 1, 1, 3, 4],
             [1, 1, 1, 3, 4]]

    d, p = floyd_warshall(weights)
    assert (d, p) == (dists, preds)
    assert restore_path(0, 4, p) == [0, 2, 1, 4]

def test_floyd_warshall_missing_paths():
    dists = [[0, 3, 2, 3],
             [float('inf'), 0, float('inf'), float('inf')],
             [float('inf'), 6, 0, 1],
             [float('inf'), 5, 1, 2]]

    preds = [[0, 1, 2, 2],
             [-1, 1, -1, -1],
             [-1, 3, 2, 3],
             [-1, 1, 2, 2]]

    d, p = floyd_warshall(missing_paths)
    assert (d, p) == (dists, preds)
    assert restore_path(1, 0, p) == None

def test_floyd_warshall_negative_weight():
    dists = [[0, 7, 4], [2, 0, -3], [5, 12, 0]]
    preds = [[0, 1, 1], [2, 1, 2], [0, 0, 2]]

    d, p = floyd_warshall(negative)
    assert (d, p) == (dists, preds)
    assert restore_path(0, 2, p) == [0, 1, 2]