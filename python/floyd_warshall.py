"""
Assumes no negative weights cycles, but may contain negative weight edges
Time Complexity: O(V^3)
Space Complexity: O(V^2)

"""

import math
import copy
from itertools import product

def floyd_warshall(weights):
    n = len(weights)
    d = copy.deepcopy(weights)
    p = [[-1] * n for i in range(n)]

    for i, j in product(range(n), repeat=2):
        if d[i][j] != float('inf'):
            p[i][j] = j

    for k, i, j in product(range(n), repeat=3):
        new_dist = d[i][k] + d[k][j]
        if new_dist < d[i][j]:
            d[i][j] = new_dist
            p[i][j] = p[i][k]

    return d, p


def restore_path(start, end, p):
    if p[start][end] == -1:
        return None
    
    path = [start]  
    while path[-1] != end:
        path.append(p[path[-1]][end])

    return path
