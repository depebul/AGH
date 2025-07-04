from kol1testy import runtests

def maxrank(T):
    n = len(T)

    if n == 0:
        return 0

    # Tworzenie listy par (wartość, oryginalny indeks)
    indexed_T = [(T[i], i) for i in range(n)]

    # Sortowanie według wartości (jeśli wartości są równe, sortowanie według indeksów)
    indexed_T.sort()

    # Tablica do przechowywania rankingu
    rank = [0] * n

    # Liczenie rangi
    for i in range(n):
        _, original_index = indexed_T[i]
        rank[original_index] = i

    # Tablica do przechowywania liczby elementów mniejszych niż bieżący element
    smaller_count = [0] * n

    for i in range(1, n):
        smaller_count[i] = smaller_count[i - 1]
        if T[indexed_T[i][1]] != T[indexed_T[i - 1][1]]:
            smaller_count[i] += 1

    # Zwracamy maksymalną rangę
    return max(smaller_count)

runtests( maxrank, all_tests = True )