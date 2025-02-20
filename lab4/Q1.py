class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices  for _ in range(num_vertices)]

    def addEdge(self, u, v):
        self.graph[u][v] = 1
    
    def dls_helper(self, current, goal, depth_limit, visited):
        if current == goal:
            return [goal]
        if depth_limit <= 0:
            return None
        visited.add(current)
        for neighbour in range(self.num_vertices):
            if self.graph[current][neighbour] and neighbour not in visited:
                path = self.dls_helper(neighbour, goal, depth_limit, visited)
                if path:
                    return [current]+path
        visited.remove(current)
        return None

    def depth_limited_search(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            visited = set()
            path = self._dls_helper(start, goal, depth, visited)
            print(f"Depth Level {depth}: {path}")
            if path:
                return path
        return None

if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    print("Depth-Limited Search Path:", g.depth_limited_search(0, 5, 3))