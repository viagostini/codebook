"""
Assumes no negative weights
Time Complexity: O(V + E log V)
Space Complexity: O(V)

"""

import heapq

def dijkstra(adj, start):
    path = {vertex: -1 for vertex in adj}
    dist = {vertex: float('inf') for vertex in adj}

    dist[start] = 0

    pq = [(0, start)]
    while len(pq) > 0:
        lenght, vertex = heapq.heappop(pq)

        if lenght > dist[vertex]:
            continue

        for child, weight in adj[vertex]:
            new_dist = lenght + weight

            if new_dist < dist[child]:
                dist[child] = new_dist
                path[child] = vertex
                heapq.heappush(pq, (new_dist, child))

    return dist, path

def restore_path(start, end, p):
    path = []

    v = end
    while v != start:
        path.append(v)
        v = p[v]
    path.append(start)

    return path[::-1]
