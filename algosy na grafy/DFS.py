# DFS
def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    time = 0

    def DFSVisit(G, u):
        nonlocal time
        time += 1
        print(u, time)
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisit(G, v)

        time += 1

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)

    return visited, parent


G = [
    [1, 4],
    [0, 2],
    [1, 3, 5],
    [2, 4],
    [0, 5],
    [2, 4, 6],
    [5, 7],
    [6]
]
print(DFS(G))