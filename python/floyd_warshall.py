import math
import copy

dist = [
    [0, 9, 1, 30, float('inf')],
    [9, 0, 7, 3, 10],
    [1, 7, 0, 15, float('inf')],
    [30, 3, 15, 0, 8],
    [float('inf'), 10, float('inf'), 8, 0]
]

def floyd_warshall(weights):
    n = len(weights)
    d = copy.deepcopy(weights)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d

dists = floyd_warshall(dist)
print(dists)
print(dist)