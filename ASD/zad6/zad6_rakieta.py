from zad6testy import runtests
from queue import PriorityQueue

def jumper( G, s, w ):
    n = len(G)
    G2 = [[0] * n for _ in range(n)]
    for u in range(n):
        for v in range(n):
            for x in range(u + 1, n):
                if G[u][v] != 0 and G[v][x] != 0 and u != x:
                    mx = max(G[u][v], G[v][x])
                    if G2[u][x] == 0 or mx < G2[u][x]:
                        G2[u][x] = mx
                        G2[x][u] = mx

    pq = PriorityQueue()
    dist = [float('inf')] * n
    dist[s] = 0
    dist_jump = [float('inf')] * n
    dist_jump[s] = 0
    pq.put((0, s, True))
    while not pq.empty():
        d, u, can_jump = pq.get()
        if u == w:
            break
        if can_jump:
            for v in range(n):
                t = G2[u][v]
                if t == 0:
                    continue
                new_d = d + t
                if new_d < dist[v]:
                    dist[v] = new_d
                    pq.put((new_d, v, False))
        for v in range(n):
            t = G[u][v]
            if t == 0:
                continue
            new_d = d + t
            if new_d < dist_jump[v]:
                dist_jump[v] = new_d
                if dist_jump[v] < dist[v]:
                    dist[v] = dist_jump[v]
                pq.put((new_d, v, True))
    return min(dist_jump[w], dist[w])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )