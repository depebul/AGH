from egzP3btesty import runtests 
from queue import PriorityQueue


def lufthansa ( G ):
    tab = []
    for i in range(len(G)):
        for el in G[i]:
            if el[0] > i:
                tab.append([el[0],i,el[1]])
    def find(x, p):
        if p[x] == -1:
            return -1
        while x != p[x]:
            x = p[x]
        return x
    def union(x, y, p, rank):
        x = find(x, p)
        y = find(y, p)
        if rank[x] > rank[y]:
            p[y] = x
        else:
            p[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1
    def kruskal(E, n):
        in_mst = [False] * len(E)
        E = sorted(E, key=lambda x: -x[2])
        rank = [0] * n
        parent = [i for i in range(n)]
        parent[0] = 0
        MST = []
        for i in range(len(E)):
            e = E[i]
            if find(e[0], parent) != find(e[1], parent):
                union(e[0], e[1], parent, rank)
                MST.append(e)
                in_mst[i] = True
        return MST, in_mst
    tab.sort(key=lambda x: -x[2])
    MST, in_mst = kruskal(tab, len(G))
    for i in range(len(in_mst)):
        if in_mst[i] == False:
            print()
            return sum([el[2] for el in tab]) - sum([el[2] for el in MST]) - tab[i][2]
    return 0

runtests ( lufthansa, all_tests=True )