from graphs.dijkstra import *

adj = {
    0: [ (1, 9), (2, 1), (3, 30) ],
    1: [ (0, 9), (2, 7), (3, 3), (4, 10) ],
    2: [ (0, 1), (1, 7), (3, 15) ],
    3: [ (0, 30), (1, 3), (2, 15), (4, 8) ],
    4: [ (1, 10), (3, 8) ]
}

def test_dijkstra_zero():
    dists = {0: 0, 1: 8, 2: 1, 3: 11, 4: 18}
    preds = {0: -1, 1: 2, 2: 0, 3: 1, 4: 1}
    assert dijkstra(adj, 0) == (dists, preds)

def test_dijkstra_one():
    dists = {0: 8, 1: 0, 2: 7, 3: 3, 4: 10}
    preds = {0: 2, 1: -1, 2: 1, 3: 1, 4: 1}
    assert dijkstra(adj, 1) == (dists, preds)

def test_dijkstra_two():
    dists = {0: 1, 1: 7, 2: 0, 3: 10, 4: 17}
    preds = {0: 2, 1: 2, 2: -1, 3: 1, 4: 1}
    assert dijkstra(adj, 2) == (dists, preds)

def test_dijkstra_three():
    dists = {0: 11, 1: 3, 2: 10, 3: 0, 4: 8}
    preds = {0: 2, 1: 3, 2: 1, 3: -1, 4: 3}
    assert dijkstra(adj, 3) == (dists, preds)

def test_dijkstra_four():
    dists = {0: 18, 1: 10, 2: 17, 3: 8, 4: 0}
    preds = {0: 2, 1: 4, 2: 1, 3: 4, 4: -1}
    assert dijkstra(adj, 4) == (dists, preds)

def test_restore_path():
    preds = {0: -1, 1: 2, 2: 0, 3: 1, 4: 1}
    path_one = [0, 2, 1]
    path_two = [0, 2]
    path_three = [0, 2, 1, 3]
    path_four = [0, 2, 1, 4]
    assert restore_path(0, 1, preds) == path_one
    assert restore_path(0, 2, preds) == path_two
    assert restore_path(0, 3, preds) == path_three
    assert restore_path(0, 4, preds) == path_four
