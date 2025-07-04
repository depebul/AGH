# cykl Eulera
def find_cycle(G, start_v):
    n = len(G)
    cycle = []

    def DFSVisit(G, u):
        nonlocal cycle

        for i in range(n):
            if G[u][i] != 0:
                G[u][i] = 0
                G[i][u] = 0
                DFSVisit(G, i)

        cycle.append(u)

    matrix_graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            matrix_graph[i][j] = 1

    DFSVisit(matrix_graph, start_v)

    return cycle[::-1]


G = [
    [1, 2],
    [0, 2, 3, 4, 5, 6],
    [0, 1, 3, 4, 5, 6],
    [1, 2, 4, 5],
    [1, 2, 3, 5],
    [1, 2, 3, 4],
    [1, 2]
]
start_v = 0
print(find_cycle(G, start_v))