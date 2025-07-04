# Dawid Żak, mój algorytm tworzy nowy graf który posiada ścieżki przy użyciu butów, następnie sprawdza wszystkie ścieżki
# zarówno z butami jak i bez przy użyciu dijkstry. złożoność czasowa to O(V^3), a pamięciowa to O(V^2).

from zad6testy import runtests
from queue import PriorityQueue
def jumper(G, s, w):
    def create_graph_with_boots(G):
        new_G = [[0 for _ in range(len(G))] for _ in range(len(G))]
        for v in range(len(G)):
            for u in range(len(G)):
                if G[v][u] != 0:
                    for w in range(len(G)):
                        if G[u][w] != 0 and w != v:
                            if new_G[v][w] == 0:
                                new_G[v][w] = max(G[v][u], G[u][w])
                            else:
                                new_G[v][w] = min(new_G[v][w], max(G[v][u], G[u][w]))
        return new_G
    new_G = create_graph_with_boots(G)
    q = PriorityQueue()
    visited = [False] * len(G)
    visited_boots = [False] * len(G)
    q.put((0, s, False))
    do_w = float("inf")
    while not q.empty():
        dist, u, way = q.get()
        if u == w:
            do_w = min(do_w, dist)
        if visited[w] and visited_boots[w]:
            return do_w
        if way:
            visited_boots[u] = True
        else:
            visited[u] = True
        for i in range(len(G)):
            if G[u][i] != 0:
                if not visited[i]:
                    q.put((dist + G[u][i], i, False))
        if not way:
            for i in range(len(G)):
                if new_G[u][i] != 0:
                    if not visited_boots[i]:
                        q.put((dist + new_G[u][i], i, True))
    return do_w
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )