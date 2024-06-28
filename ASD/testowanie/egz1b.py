# Dawid Żak, mój algorytm najpierw tworzy tablice zawierającą wszystkie możliwe podciągi,
# następnie zlicza dla każdego z nich sume z osobna, żeby potem posortować wszystkie
# elementy w podciągu do osobnej tablicy i odejmować z niej elementy aż otrzymamy
# największą wartość dla sumy danego podciągu ( po odjęciu conajwyżej k elementów ),
# potem porówuje z największą wartością sum wszystkich możliwych podciągów.
# złożoność czasowa to O(n^3logn).

from egz1btesty import runtests
from math import inf


def kstrong(T, k):
    podciagi = []
    n = len(T)
    for i in range(n):
        for j in range(i + 1, n + 1):
            podciagi.append(T[i:j])
    max_val = -inf
    for podciag in podciagi:
        sum = 0
        for liczba in podciag:
            sum += liczba
        sorted_podciag = sorted(podciag)
        for i in range(min(k, len(podciag))):
            sum = max(sum, sum - sorted_podciag[i])
        max_val = max(sum, max_val)
    return max_val


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kstrong, all_tests=True)
