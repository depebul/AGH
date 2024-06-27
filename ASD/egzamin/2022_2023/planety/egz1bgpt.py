from egz1btesty import runtests
import heapq

import heapq

def planets(D, C, T, E):
    n = len(D)
    inf = float('inf')

    # Minimalny koszt podróży do każdej z planet
    min_cost = [inf] * n
    min_cost[0] = 0  # Startujemy z planety A, więc koszt początkowy to 0

    # Kolejka priorytetowa do przetwarzania planet
    pq = [(0, 0)]  # (koszt, numer planety)

    while pq:
        current_cost, planet = heapq.heappop(pq)

        if current_cost > min_cost[planet]:
            continue

        # Sprawdzamy wszystkie możliwe tankowania i loty do następnych planet
        for next_planet in range(planet + 1, n):
            distance = D[next_planet] - D[planet]
            if distance > E:
                break  # Nie możemy dolecieć do tej planety bezpośrednio

            fuel_cost = distance * C[planet]
            new_cost = current_cost + fuel_cost

            if new_cost < min_cost[next_planet]:
                min_cost[next_planet] = new_cost
                heapq.heappush(pq, (new_cost, next_planet))

        # Sprawdzamy możliwość użycia teleportu
        j, teleport_cost = T[planet]
        if j >= planet:
            new_cost = current_cost + teleport_cost
            if new_cost < min_cost[j]:
                min_cost[j] = new_cost
                heapq.heappush(pq, (new_cost, j))

    return min_cost[-1]
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )