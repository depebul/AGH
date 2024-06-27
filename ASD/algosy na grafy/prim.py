# Prim
from queue import PriorityQueue

def relax(v, distance, u_v_distance):
    if distance[v] >= u_v_distance:
        distance[v] = u_v_distance
        return True
    return False

def prim(G, start):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    MST = []

    distance[start] = 0
    visited[start] = True
    Q = PriorityQueue()

    for i in range(n):
        Q.put((distance[i], i))

    while not Q.empty():
        u_distance, u = Q.get()
        MST.append((parent[u], u, u_distance))
        for v_data in G[u]:
            v, u_v_distance = v_data
            if not visited[v] and relax(v, distance, u_v_distance):
                parent[v] = u
                visited[v] = True
                Q.put((distance[v], v))

    return MST