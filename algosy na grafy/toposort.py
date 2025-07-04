# sortowanie topologiczne
def DAG_sorting(G):
    n = len(G)
    visited = [False for _ in range(n)]
    sorted_G = []

    def DFSVisit(G, u):
        nonlocal sorted_G

        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v)

        sorted_G.append(u)



    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)

    return sorted_G[::-1]

G = [
    [1, 2, 5],
    [2, 4],
    [],
    [],
    [3, 6],
    [4],
    []
]
print(DAG_sorting(G))