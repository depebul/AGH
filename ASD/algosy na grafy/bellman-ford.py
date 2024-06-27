# Bellman - Ford
def relax(u, v, distance, edge_dist):
    if distance[u] > distance[v] + edge_dist:
        distance[u] = distance[v] + edge_dist
        return True
    return False

def bf(G, s):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]

    distance[s] = 0

    for v in range(n - 1):
        for u_data in G[v]:
            u, u_edge_dist = u_data
            relax(u, v, distance, u)

    for v in range(n):
        for u_data in G[v]:
            u, u_dist_edge = u_data
            if distance[u] <= distance[v] + u_dist_edge:
                return -1

    return distance