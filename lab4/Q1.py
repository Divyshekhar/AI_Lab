def dls(graph, node, depth, visited, path, traversal):
    if depth < 0:
        return False
    
    visited[node] = True
    path.append(node)
    traversal.append(node)
    
    if depth == 0:
        return True
    
    for neighbor, is_connected in enumerate(graph[node]):
        if is_connected and not visited[neighbor]:
            if dls(graph, neighbor, depth - 1, visited, path, traversal):
                return True
    
    path.pop()
    visited[node] = False
    return False

def iterative_dls(graph, start):
    num_nodes = len(graph)
    for depth in range(num_nodes):
        visited = [False] * num_nodes
        path = []
        traversal = []
        dls(graph, start, depth, visited, path, traversal)
        print(f"Traversal at depth {depth}: {traversal}")

# Example usage:
adjacency_matrix = [
    [0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0]
]

start_node = 0
iterative_dls(adjacency_matrix, start_node)
