from egz3btesty import runtests
from math import inf
from collections import deque

def maze(L):
    n = len(L)
    dol_tab = [[-1 for _ in range(n)] for _ in range(n)]
    gora_tab = [[-1 for _ in range(n)] for _ in range(n)]
    gora_tab[0][0] = dol_tab[0][0] = 0
    for i in range(n):
        for j in range(n):
            if L[i][j] == '#':
                dol_tab[i][j] = float("-inf")
                gora_tab[i][j] = float("-inf")

    def gora(y, x):
        if not (x < 0 or y < 0 or x > n or y > n or L[y][x] == '#'):
            if gora_tab[y][x] != -1:
                return gora_tab[y][x]
            gora_tab[y][x] = max(prawo(y, x - 1) + 1, gora(y - 1, x) + 1)
            return gora_tab[y][x]
        return float("-inf")

    def dol(y, x):
        if not (x < 0 or y < 0 or x >= n or y >= n or L[y][x] == '#'):
            if dol_tab[y][x] != -1:
                return dol_tab[y][x]
            dol_tab[y][x] = max(prawo(y, x - 1) + 1, dol(y + 1, x) + 1)
            return dol_tab[y][x]
        return float("-inf")

    def prawo(y, x):
        return max(dol(y, x), gora(y, x))

    ok = prawo(n - 1, n - 1)
    return ok if ok > 0 else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
