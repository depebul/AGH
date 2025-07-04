# Dawid Żak, mój algorytm najpierw zamienia listę krawędzi na listę sąsiedztwa, następnie przy pomocy algorytmu DFS
# zmodyfikowanego aby sprawdzał także czy dany lot jest możliwy poprzez porównywanie zakresów
# wysokości na których musiałby się znaleźć samolot. Jeśli dany lot jest możliwy algorytm
# zostaje przerwany i zwraca True, jeśli nie to zwraca False. Złożoność czasowa to O(E!), złożoność pamięciowa to
# O(E).

from zad4testy import runtests


def Flight(L, x, y, t):
    n = max(L, key=lambda x: x[1])[1] + 1
    neighbours = [[] for _ in range(n)]
    for i in range(len(L)):
        neighbours[L[i][0]].append([L[i][1], L[i][2]])
        neighbours[L[i][1]].append([L[i][0], L[i][2]])
    works = False
    visited = [False] * n

    def DFS(G, start, t, y, visited, min_t=float("-inf"), max_t=float("inf")):
        nonlocal works
        if works:
            return
        visited[start] = True
        for i in range(len(G[start])):
            if not visited[G[start][i][0]]:
                if G[start][i][1] - t > max_t or G[start][i][1] + t < min_t:
                    continue
                if G[start][i][0] == y:
                    works = True
                    return
                min_loc = max(min_t, G[start][i][1] - t)
                max_loc = min(max_t, G[start][i][1] + t)
                DFS(G, G[start][i][0], t, y, visited, min_loc, max_loc)
        visited[start] = False

    DFS(neighbours, x, t, y, visited)
    return works


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(Flight, all_tests=True)
