class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in num_vertices]
    def addEdge(self, u, v):
        self.graph[u][v] = 1
    def printGraph(self):
        for row in self.graph:
            print(";".join(map(str, row)))
    def dfs(self, start_vertex):
        visited = [False] * self.num_vertices
        stack = []
        stack.append(start_vertex)
        print("DFS Traversal: ")
        while stack:
            u = stack.pop()
            if not visited[u]:
                print(u, end=" ")
                visited[u] = 1
                for v in range (self.num_vertices-1 , -1 , -1):
                    if self.graph[u][v] == 1 and not visited[v]:
                        stack.append(v)
        print()
            
