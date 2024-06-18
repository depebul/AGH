from kol2testy import runtests

from queue import PriorityQueue

def warrior(G, s, t):
    n = max(max(u, v) for u, v, w in G) + 1
    neighbours = [[] for _ in range(n)]
    for u, v, w in G:
        neighbours[u].append((v, w))
        neighbours[v].append((u, w))

    distance = [float("inf")] * n
    distance[s] = 0
    q = PriorityQueue()
    q.put((0, s, 16))

    while not q.empty():
        dist, u, remaining = q.get()
        if dist != distance[u]:
            continue
        for v, w in neighbours[u]:
            if remaining >= w and dist + w < distance[v]:
                distance[v] = dist + w
                q.put((distance[v], v, remaining - w))
            elif remaining < w and dist + w + 8 < distance[v]:
                distance[v] = dist + w + 8
                q.put((distance[v], v, 16))

    return distance[t] if distance[t] != float("inf") else None
runtests( warrior, all_tests = True )