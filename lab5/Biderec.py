def build_graph(adjacency_matrix):
    graph = [[] for _ in range(len(adjacency_matrix))]
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1:
                graph[i].append(j)
    return graph

def bfs(queue, visited, parent, graph):
    current = queue.pop(0)
    for neighbor in graph[current]:
        if not visited[neighbor]:
            queue.append(neighbor)
            visited[neighbor] = True
            parent[neighbor] = current

def is_intersecting(src_visited, dest_visited):
    for i in range(len(src_visited)):
        if src_visited[i] and dest_visited[i]:
            return i
    return -1

def print_path(intersecting_node, src, dest, src_parent, dest_parent):
    path = []
    i = intersecting_node

    while i != src:
        path.append(i)
        i = src_parent[i]
    path.append(src)
    path.reverse()

    i = intersecting_node
    while i != dest:
        i = dest_parent[i]
        path.append(i)

    print("Path")
    print(" ".join(map(str, path)))

def bidirectional_search(adjacency_matrix, src, dest):
    n = len(adjacency_matrix)
    graph = build_graph(adjacency_matrix)
    src_queue = [src]
    dest_queue = [dest]

    src_visited = [False] * n
    dest_visited = [False] * n

    src_parent = [None] * n
    dest_parent = [None] * n

    src_visited[src] = True
    dest_visited[dest] = True

    while src_queue and dest_queue:
        bfs(src_queue, src_visited, src_parent, graph)
        bfs(dest_queue, dest_visited, dest_parent, graph)

        intersecting_node = is_intersecting(src_visited, dest_visited)
        if intersecting_node != -1:
            print(f"Path exists between {src} and {dest}")
            print(f"Intersection at: {intersecting_node}")
            print_path(intersecting_node, src, dest, src_parent, dest_parent)
            return

    print(f"Path does not exist between {src} and {dest}")

if __name__ == '__main__':
    adjacency_matrix = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    ]


    src = 0
    dest = 14

    bidirectional_search(adjacency_matrix, src, dest)
