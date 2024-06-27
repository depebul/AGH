from egz2btesty import runtests
from math import inf
def magic( C ):
    n = len(C)
    tab = [-inf for _ in range(n)]
    tab[0] = 0
    for i in range(n):
        G = C[i][0]
        for j in range(1,4):
            k,w = C[i][j]
            if w != -1 and tab[i] + G - k >= 0 and G - k <= 10:
                tab[w] = max(tab[w],tab[i] + G - k)
    return tab[-1] if tab[-1] != -inf else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
