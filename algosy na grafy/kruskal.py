# najmniejsze drzewo rozpinające, czyli jak ma być nieoptymalna ścieżka z a do b ale tylko jedna
# jak minus w sortowaniu to największe drzewo rozpinające, czyli jak ma być optymalna ścieżka z a do b ale tylko jedna
# działa to na liście krawędzi
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
    E = sorted(E, key=lambda x: x[2])
    rank = [0] * n
    p = [i for i in range(n)]
    p[0] = 0
    answer = []
    for e in E:
        if find(e[0], p) != find(e[1], p):
            union(e[0], e[1], p, rank)
            answer.append(e)
    return answer