def dfs(adj, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    yield start
    for child in adj[start] - visited:
        yield from dfs(adj, child, visited)
    
    #return visited
    
def dfs_iter(adj, start):
    visited, stack = set(), [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(adj[node] - visited)

    return visited
