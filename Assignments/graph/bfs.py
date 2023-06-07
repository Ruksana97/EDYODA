from collections import defaultdict

class Graph:


    def __init__(self):

        self.graph = defaultdict(list)


    def addEdge(self, a, b):
        self.graph[a].append(b)
        self.visited = []


    def BFS(self, f):


        queue = []


        queue.append(f)
        self.visited.append(f)

        while queue:


            f = queue.pop(0)
            print(f, end=" ")


            for i in self.graph[f]:
                if i not in self.visited:
                    queue.append(i)
                    self.visited.append(f)



gph = Graph()
gph.addEdge(0, 1)
gph.addEdge(0, 2)
gph.addEdge(1, 2)
gph.addEdge(2, 0)
gph.addEdge(2, 3)
gph.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
gph.BFS(2)
