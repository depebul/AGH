from kolutesty import runtests


def projects(n, L):
    tab = [[] for _ in range(n)]
    for i in range(len(L)):
        tab[L[i][1]].append(L[i][0])
    def toposort(tab):
        visited = [False] * len(tab)
        tab2 = []
        def dfs(v):
            visited[v] = True
            for u in tab[v]:
                if not visited[u]:
                    dfs(u)
            tab2.append(v)
        for i in range(n):
            if not visited[i]:
                dfs(i)
        return tab2[::-1]
    max_length = [1] * n
    print(tab if n == 4 else "nie")
    tab2 = toposort(tab)
    for i in tab2:
        for j in tab[i]:
            max_length[j] = max(max_length[j], max_length[i] + 1)
    return max(max_length)
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(projects, all_tests=True)
