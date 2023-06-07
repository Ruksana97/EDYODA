def addEdge(adj_matrix, a, b):
    adj_matrix[a].append(b)
    adj_matrix[a].append(b)



def DFS1(a, adj_matrix, visited):
    visited[a] = True
    for i in range(len(adj_matrix[a])):
        if (visited[adj_matrix[a][i]] == False):
            DFS1(adj_matrix[a][i], adj_matrix, visited)



def countTrees(adj_matrix, Vertices):
    visited = [False] * Vertices
    res = 0
    for a in range(Vertices):
        if (visited[a] == False):
            DFS1(a, adj_matrix, visited)
            res += 1
    return res



Vertices = 5
adj_matrix = [[] for i in range(Vertices)]
addEdge(adj_matrix, 0, 1)
addEdge(adj_matrix, 0, 2)
addEdge(adj_matrix, 3, 4)
print(countTrees(adj_matrix, Vertices))
