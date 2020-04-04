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