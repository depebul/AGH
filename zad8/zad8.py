# Dawid Żak, mój algortym najpierw tworzy tablicę tab, następnie ustala wartości dla pierwszego wiersza,
# potem iteruje po wierszach, zmienna "a" pozwala nam być pewnym że nie użyjemy dwa razy tego samego parkingu,
# ponieważ jedyna opcja na wzięcie optymalnej wartości to albo z górnej lewej komórki albo poprostu z górnej komórki.
# Złożoność czasowa to O(n*m)

from zad8testy import runtests


def parking(X, Y):
    n = len(X)
    m = len(Y)
    tab = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(m):
        tab[0][j] = abs(X[0] - Y[j])
    for i in range(1, n):
        a = tab[i - 1][i - 1]
        for j in range(i, m):
            tab[i][j] = a + abs(X[i] - Y[j])
            a = min(a, tab[i - 1][j])
    return min(filter(lambda x: x != 0, tab[n - 1]))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)
