# spójne składowe
def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    time = 1

    def DFSVisit(G, v):
        nonlocal time

        time += 1
        visited[v] = True

        for u in G[v]:
            if not visited[v]:
                DFSVisit(G, u)

        distance[v] = time
        time += 1

        for i in range(n):
            if not visited[i]:
                DFSVisit(G, i)

    return distance

def reverse_edge(G):
    n = len(G)
    reverse_G = [[] for _ in range(n)]

    for v in range(n):
        for u in G[v]:
            reverse_G[u].append(v)

    return reverse_G

def spojne(G):
    times = DFS(G)
    reverse_G = reverse_edge(G)


G = [
    [1, 4],
    [2],
    [0, 7],
    [4, 6],
    [5],
    [3, 6],
    [8],
    [3, 9],
    [5, 10],
    [7]
]