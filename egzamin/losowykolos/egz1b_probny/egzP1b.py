from egzP1btesty import runtests 
from math import inf
from queue import PriorityQueue
def turysta( G, D, L ):
    size = 0
    for i in range(len(G)):
        size = max(size, G[i][0], G[i][1])
    tab = [[] for _ in range(size + 1)]
    for first, second, weight in G:
        tab[first].append((second, weight))
        tab[second].append((first, weight))
    distance = [[inf,inf,inf,inf,inf] for _ in range(size + 1)]
    distance[D] = [0,0,0,0,0]
    pq = PriorityQueue()
    pq.put((0,0,D))
    while not pq.empty():
        d,t, u = pq.get()
        if t == 4:
            continue
        for v, cost in tab[u]:
            if distance[v][t + 1] > d + cost:
                distance[v][t + 1] = d + cost
                pq.put((distance[v][t + 1],t + 1 , v))
    return distance[L][4] if distance[L][4] != inf else -1
runtests ( turysta )