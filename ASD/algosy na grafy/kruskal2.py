# Kruskal
def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent, rank):
    x = find(x, parent)
    y = find(y, parent)

    if x == y: return
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def make_edges_list(G):
    n = len(G)
    edges = []

    for v in range(n):
        for u_data in G[v]:
            u, u_v_dist = u_data
            edges.append((u_v_dist, v, u))

    return edges

def kruskal(G):
    n = len(G)
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    A = []
    min_weight = 0
    taken = 0

    edges = make_edges_list(G)
    edges.sort()

    for edge in edges:
        if taken == n - 1:
            return A, min_weight
        u, v, distance = edge
        u = find(u, parent)
        v = find(v, parent)

        if u != v:
            union(u, v, parent, rank)
            A.append(edge)
            taken += 1
            min_weight += distance

    return A, min_weight