from collections import defaultdict
class Graph:


    def __init__(self):


        self.graph = defaultdict(list)


    def addEdge(self, a, b):
        self.graph[a].append(b)


    def DFS1(self, b, visited):


        visited[b] = True
        print(b)




        for i in self.graph[b]:
            if visited[i] == False:
                self.DFS1(i, visited)


    def DFS(self):
        tot_vertices= len(self.graph)
        visited = [False] * (tot_vertices)


        for i in range(tot_vertices):
            if visited[i] == False:
                self.DFS1(i, visited)



gph = Graph()
gph.addEdge(0, 1)
gph.addEdge(0, 2)
gph.addEdge(1, 2)
gph.addEdge(2, 0)
gph.addEdge(2, 3)
gph.addEdge(3, 3)

print("Depth First Traversal is:")
gph.DFS()