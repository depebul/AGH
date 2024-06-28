# Dawid Żak, mój algorytm najpierw przerabia liste krawędzi na liste sąsiedztwa,
# następnie wykonuje dijkstre i oblicza odległość do każdego wierzchołka z punktu s
# potem to samo wykonuje startując z punktu t, potem sprawdzamy jaki jest najbardziej
# optymalny rower do wzięcia dla każdego wierzchołka z rowerami i końcowo
# liczymy jaka jest najszybsza trasa dodając wynik z tablicy dist ( od s ) do tablicy
# dist2 ( od t ) pomnożony razy najbardziej optymalny rower z tamtego miejsca
# (to wykonujemy tylko dla miejsce które są w talicy B )
# do tego jeszcze liczymy min z wartości trasy z rowerem i tej bez rowera.
# złożoność czasowa to O(ElogV)

from egz1atesty import runtests
from queue import PriorityQueue
from math import inf
from math import floor


def armstrong(B, G, s, t):
    n = -inf
    for i in range(len(G)):
        n = max(n, G[i][0], G[i][1])
    n += 1
    tab = [[] for _ in range(n)]
    for i in range(len(G)):
        el = G[i]
        tab[el[0]].append([el[1], el[2]])
        tab[el[1]].append([el[0], el[2]])

    dist = [inf] * n
    dist[s] = 0
    pq = PriorityQueue()
    pq.put((0, s))
    while not pq.empty():
        d, u = pq.get()
        for v, cost in tab[u]:
            if dist[v] > d + cost:
                dist[v] = d + cost
                pq.put((dist[v], v))
    dist2 = [inf] * n
    dist2[t] = 0
    pq.put((0, t))
    while not pq.empty():
        d, u = pq.get()
        for v, cost in tab[u]:
            if dist2[v] > d + cost:
                dist2[v] = d + cost
                pq.put((dist2[v], v))
    ride_tab = [inf] * len(tab)
    for i in range(len(B)):
        ride_tab[B[i][0]] = min(ride_tab[B[i][0]], B[i][1] / B[i][2])
    min_val = inf
    for i in range(len(ride_tab)):
        if ride_tab != inf:
            min_val = min(min_val, dist[i] + ride_tab[i] * dist2[i])
    min_val = min(min_val, dist[t])
    return floor(min_val)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(armstrong, all_tests=True)
