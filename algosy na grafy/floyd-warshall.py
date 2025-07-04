# Floyd - Warshall
def fw(G):
    n = len(G)
    for k in range(1, n + 1):
        for x in range(n):
            for y in range(n):
                G[x][y] = min(G[x][y], G[x][k] + G[k][v])

    return G