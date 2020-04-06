def bfs(adj, start):
    visited, queue = set(), [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(adj[node] - visited)

    return visited