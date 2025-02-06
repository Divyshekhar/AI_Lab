class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]  

    def addEdge(self, u, v):
        self.graph[u][v] = 1 

    def printGraph(self):
        print("Adjacency Matrix:")
        for row in self.graph:
            print(" ".join(map(str, row)))

    def BFS(self, start_vertex):
        visited = [False] * self.num_vertices
        queue = []
        queue.append(start_vertex)
        visited[start_vertex] = True

        print("BFS Traversal:")
        while queue:
            u = queue.pop(0)
            print(u, end=" ")

            for v in range(self.num_vertices):
                if self.graph[u][v] == 1 and not visited[v]:
                    queue.append(v)
                    visited[v] = True

if __name__ == '__main__':
    num_vertices = int(input("Enter the number of vertices in the graph: "))
    g = Graph(num_vertices)

    num_edges = int(input("Enter the number of edges in the graph: "))
    print("Enter each edge as u v:")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        g.addEdge(u, v)

    print("\nThe graph you have entered is:")
    g.printGraph()

    start_vertex = int(input("\nEnter the starting vertex for BFS: "))
    g.BFS(start_vertex)
