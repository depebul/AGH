from kol2testy import runtests

import heapq
from collections import defaultdict, deque

def warrior(G, s, t):
    # Tworzenie grafu z listy krawędzi
    graph = defaultdict(list)
    for u, v, w in G:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # Kolejka priorytetowa (min-heap)
    heap = [(0, s, 0)]  # (total_time, current_node, hours_without_rest)
    visited = defaultdict(lambda: float('inf'))  # Słownik do śledzenia odwiedzonych stanów

    while heap:
        total_time, u, hours_without_rest = heapq.heappop(heap)

        # Jeśli dotarliśmy do miasteczka t, zwracamy całkowity czas podróży
        if u == t:
            return total_time

        if visited[(u, hours_without_rest)] <= total_time:
            continue
        visited[(u, hours_without_rest)] = total_time

        for v, w in graph[u]:
            new_hours_without_rest = hours_without_rest + w

            if new_hours_without_rest > 16:
                # Musimy odpocząć w schronisku (czyli u jest schroniskiem)
                new_hours_without_rest = w
                new_total_time = total_time + w + 8  # 8 godzin odpoczynku
            else:
                new_total_time = total_time + w

            if visited[(v, new_hours_without_rest)] > new_total_time:
                heapq.heappush(heap, (new_total_time, v, new_hours_without_rest))

    return float('inf')  # Jeśli nie ma możliwej drogi, zwracamy nieskończoność

runtests( warrior, all_tests = True )