from kol2testy import runtests
from queue import PriorityQueue

def warrior( G, s, t):
    E = G
    a = s
    b = t
    n = max(max(E, key=lambda x: x[0])[0], max(E, key=lambda x: x[1])[1]) + 1
    G = [[] for _ in range(n)]
    for u, v, t in E:
        G[u].append((v, t))
        G[v].append((u, t))
    dist = [[float('inf')] * 17 for _ in range(n)]
    pq = PriorityQueue()
    # trojka (ile czasu minelo, wierzcholek, godziny do odpoczynku)
    pq.put((0, a, 16))
    while not pq.empty():
        d, u, remaining = pq.get()
        # wyciągnięcie wierzchołka b oznacza że został on już przetworzony - koniec algorytmu
        if u == b:
            return d
        # symulacja przejścia bez odpoczynku
        for v, t in G[u]:
            if remaining < t:
                continue
            new_r = remaining - t
            new_d = d + t
            if new_d < dist[v][new_r]:
                dist[v][new_r] = new_d
                pq.put((new_d, v, new_r))
        # symulacja odpoczynku
        if remaining != 16:
            pq.put((d + 8, u, 16))
    return min(dist[b])

runtests( warrior, all_tests = True )