from graphs.topological_sort import topological_sort

def assert_ordering_is_topological(ordering, adj):
    visited = set()
    for node in ordering:
        visited.add(node)
        for next_node in adj[node]:
            assert next_node not in visited

def test_topological_sort_simple():
    adj = {
        0: set(),
        1: set(),
        2: set([3]),
        3: set([1]),
        4: set([0, 1]),
        5: set([0, 2])
    }

    ordering = topological_sort(adj)
    assert_ordering_is_topological(ordering, adj)

def test_topological_sort_complicated():
    adj = {
        'A': set(['D']),
        'B': set(['D']),
        'C': set(['A', 'B']),
        'D': set(['H', 'G']),
        'E': set(['A', 'D', 'F']),
        'F': set(['J', 'K']),
        'G': set(['I']),
        'H': set(['I', 'J']),
        'I': set(['L']),
        'J': set(['L', 'M']),
        'K': set(['J']),
        'L': set(),
        'M': set(),
    }

    ordering = topological_sort(adj)
    assert_ordering_is_topological(ordering, adj)