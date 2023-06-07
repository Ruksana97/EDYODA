from collections import deque

adj_matrix = [[] for i in range(1001)]


def addEdge(a, b):

    adj_matrix[a].append(b)


    adj_matrix[b].append(a)


def BFS(c,l):
    Vertices = 100


    visited = [False] * Vertices
    level = [0] * Vertices

    for i in range(Vertices):
        visited[i] = False
        level[i] = 0


    queue = deque()

    visited[c] = True
    queue.append(c)
    level[c] = 0

    while (len(queue) > 0):


        c = queue.popleft()

        for i in adj_matrix[c]:
            if not visited[i]:

                level[i] = level[c] + 1
                visited[i] = True
                queue.append(i)

    count = 0
    for i in range(Vertices):
        if (level[i] == l):
            count += 1

    return count



addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 3)
addEdge(2, 4)
addEdge(2, 5)

level = 2
print(BFS(0, level))
