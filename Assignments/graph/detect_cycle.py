from collections import defaultdict
class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.Vertices = vertices

    def addEdge(self, a, b):
        self.graph[a].append(b)

    def isCyclic1(self, b, visited,Stack):


        visited[b] = True
        Stack[b] = True

        for i in self.graph[b]:
            if visited[i] == False:
                if self.isCyclic1(i, visited,Stack) == True:
                    return True
            elif Stack[i] == True:
                return True
        Stack[b] = False
        return False


    def isCyclic(self):
        visited = [False] * (self.Vertices + 1)
        Stack = [False] * (self.Vertices + 1)
        for j in range(self.Vertices):
            if visited[j] == False:
                if self.isCyclic1(j, visited, Stack) == True:
                    return True
        return False



gph = Graph(4)
gph.addEdge(0, 1)
gph.addEdge(0, 2)
gph.addEdge(1, 2)
gph.addEdge(2, 0)
gph.addEdge(2, 3)
gph.addEdge(3, 3)
if gph.isCyclic() == True:
        print("Graph has cycle")
else:
        print("Graph doesn't have cycle")
