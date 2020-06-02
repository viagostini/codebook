def topological_sort(adj):    
    ordering = []
    visited = set()

    for node in adj:
        if node not in visited:
            dfs(node, adj, visited, ordering)
    
    ordering.reverse()
    return ordering

def dfs(node, adj, visited, ordering):
    visited.add(node)

    for next_node in adj[node]:
        if next_node not in visited:
            dfs(next_node, adj, visited, ordering)
    
    ordering.append(node)

