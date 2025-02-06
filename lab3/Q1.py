class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
    
    def addEdge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.graph[u][v] = 1
        else:
            print(f"Error: Edge ({u}, {v}) is out of bounds!")
    
    def printGraph(self):
        print("Adjacency Matrix:")
        for row in self.graph:
            print(" ".join(map(str, row)))
    
    def DFS(self, start_vertex):
        visited = [False] * self.vertices
        stack = [start_vertex]
        
        print("DFS Traversal: ", end="")
        
        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                print(vertex, end=' ')
                visited[vertex] = True
            for i in range(self.vertices - 1, -1, -1):
                if self.graph[vertex][i] == 1 and not visited[i]:
                    stack.append(i)
        print()
if __name__ == '__main__':
    vertices = int(input("Enter the number of vertices in the graph: "))
    g = Graph(vertices)
    
    num_edge = int(input("Enter the number of edges in the graph: "))
    print("Enter each edge in the form of u v (0-based indices):")
    for _ in range(num_edge):
        u, v = map(int, input().split())
        g.addEdge(u, v)
    
    print("The entered graph is:\n")
    g.printGraph()
    
    start_vertex = int(input(f"Enter the starting vertex (0 to {vertices - 1}): "))
    if 0 <= start_vertex < vertices:
        print(f"DFS traversal starting from vertex {start_vertex} is:")
        g.DFS(start_vertex)
    else:
        print(f"Error: Starting vertex {start_vertex} is out of bounds!")
