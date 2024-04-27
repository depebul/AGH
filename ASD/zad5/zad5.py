# Dawid Żak, mój kod wykorzystuje algorytm Dijkstry, na zmienionym wcześniej grafie, gdzie wierzchołki z listy S,
# zostały połączone w jeden wierzchołek, najpierw zmodyfikowałem liste krawędzi, podmieniając wszystkie wierzchołki z
# listy S na wcześniej wybrany wierzchołek, następnie zbudowałem listę sąsiedztwa, jeśli krawędź dotyczyła wierzchołka
# z listy S, to odległość przepisywałem do tablicy broweight, przy użyciu funkcji min() i dodawałem je następnie do listy
# sąsiedztwa, następnie wykorzystałem algorytm Dijkstry, zaczynając od wierzchołka a, a kończąc na wierzchołku b.
# złożoność czasowa to O(ElogV), a pamięciowa to O(V+E), gdzie V to liczba wierzchołków, a E to liczba krawędzi.


from zad5testy import runtests
from queue import PriorityQueue

def spacetravel( n, E, S, a, b ):
    neighbours = [[] for _ in range(n)]
    isanomaly = [False]*n
    for el in S:
        isanomaly[el] = True
    if a in S and b in S:
        return 0
    elif a in S:
        name = a
    elif b in S:
        name = b
    else:
        name = S[0]
    for i in range(len(E)):
        if isanomaly[E[i][0]]:
            E[i] = (name, E[i][1], E[i][2])
        if isanomaly[E[i][1]]:
            E[i] = (E[i][0], name, E[i][2])
    broweight = [float("inf")]*n
    for i in range(len(E)):
        if isanomaly[E[i][0]]:
            broweight[E[i][1]] = min(E[i][2],broweight[E[i][1]])
        elif isanomaly[E[i][1]]:
            broweight[E[i][0]] = min(E[i][2],broweight[E[i][0]])
        else:
            neighbours[E[i][0]].append([E[i][1], E[i][2]])
            neighbours[E[i][1]].append([E[i][0], E[i][2]])
    for i in range(len(broweight)):
        if broweight[i] != float("inf"):
            neighbours[name].append([i, broweight[i]])
            neighbours[i].append([name, broweight[i]])
    q = PriorityQueue()
    distance = [float("inf")]*(len(neighbours) + 1)
    q.put((0, a))
    distance[a] = 0
    def relax(distance, v, w, u):
        if distance[v] > distance[u] + w:
            distance[v] = distance[u] + w
            return True
        return False
    while not q.empty():
        dist, u = q.get()
        for v, w in neighbours[u]:
            if relax(distance, v, w, u):
                q.put((distance[v], v))
    if distance[b] == float("inf"):
        return None
    return distance[b]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )