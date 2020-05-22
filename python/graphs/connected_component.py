from graphs.dfs import *

def connected_components(adj):
    comps = []
    visited  = set()

    node = 0
    while node < len(adj):
        if node not in visited:
            comp = set(dfs(adj, node))
            comps.append(comp)
            visited = visited.union(comp)
        node = node + 1

    return comps