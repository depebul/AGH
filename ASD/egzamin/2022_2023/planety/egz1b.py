from egz1btesty import runtests
from math import inf
def planets(D, C, T, E):
    n = len(D)
    tab = [[inf for _ in range(E + 1)] for _ in range(n)]
    for b in range(E + 1):
        tab[0][b] = C[0] * b
    tab[T[0][0]][0] = min(T[0][1], tab[T[0][0]][0])
    for i in range(1, n):
        j,p = T[i]
        for b in range(1, E + 1):
            distance = abs(D[i] - D[i - 1])
            if b >= distance:
                tab[i][b - distance] = min(tab[i][b - distance], tab[i - 1][b], tab[i][b - 1 - distance] + C[i])
        for b in range(E + 1):
            tab[i][b] = min(tab[i][b], tab[i][b - 1] + C[i])
        tab[j][0] = min(p + tab[i][0], tab[j][0])
    return min(tab[-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
