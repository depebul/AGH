#BFS
from queue import Queue

def BFS(G, s):
    Q = Queue()
    n = len(G)
    d = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    d[s] = 0
    visited[s] = True
    parent[s] = None
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.put(v)

    return d, parent, visited

G = [
    [1, 2],
    [0, 4],
    [0, 3, 5],
    [2, 4],
    [1, 3, 5],
    [2, 4, 6],
    [5, 7],
    [6]
]

s = 0
print(BFS(G, s))