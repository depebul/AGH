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