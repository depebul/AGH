# Znajdywanie mostów w grafie
def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    low = [0 for _ in range(n)]
    time = 0

    def DFSVisit(G, v):
        nonlocal time

        time += 1
        visited[v] = True
        distance[v] = time
        v_low = distance[v]
        low[v] = v_low

        min_prev = float('inf')
        min_child = float('inf')
        for u in G[v]:
            if not visited[u]:
                parent[u] = v
                DFSVisit(G, u)
                min_child = min(min_child, low[u])
            if parent[v] is not u:
                min_prev = min(min_prev, low[u])

        if parent[v] is not None:
            v_low = min(low[v], min_prev, min_child)
        low[v] = v_low

    for i in range(n):
        if not visited[i]:
            DFSVisit(G, i)

    return low, parent, distance


def find_bridge(G):
    n = len(G)
    bridges = []

    low, parent, distance = DFS(G)

    for i in range(n):
        if low[i] == distance[i] and parent[i] is not None:
            bridges.append((parent[i], i))

    return bridges

G = [
    [1, 2],
    [0, 2],
    [0, 1, 3],
    [2, 4, 5],
    [3, 5],
    [3, 4]
]

print(find_bridge(G))