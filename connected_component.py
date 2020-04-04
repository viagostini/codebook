# DFS method
# assumes graph is represented as adjacency list
# returns list with nodes in DFS order
def connected_component(adj, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    for child in adj[start] - visited:
        connected_component(adj, child, visited)
    
    return visited

def get_all_components(adj):
    comps = []
    visited  = set()

    node = 0
    while node < len(adj):
        if node not in visited:
            comp = connected_component(adj, node)
            comps.append(comp)
            visited = visited.union(comp)
        node = node + 1

    return comps