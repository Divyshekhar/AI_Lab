class Graph: 
    def __init__(self, num_vertices):
     self.num_vertices = num_vertices
     self.graph = [[0] * num_vertices for _ in range(num_vertices)]

     def addEdge(self, u, v):
        self.graph[u][v] = 1
    
    def printGraph(self):
       print("Adjacency Matrix of the Graph that you entered is")
       for row in self.graph:
          print(":".join(map(str, row)))
    
    def bfs(self, start_vertex):
        visited = [False] * self.num_vertices
        queue = []
        queue.append(start_vertex)
        visited[start_vertex] = 1
        print("BFS Traversal:")
        while queue:
           u = queue.pop(0)
           print(u, end=" ")
           visited[u] = 1
           for v in range (self.num_vertices):
              if self.graph[u][v] == 1 and not visited[v]:
                 queue.append(v)
                 visited[v] = 1
                 
