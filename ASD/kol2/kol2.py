# Dawid Żak, mój algorytm zamienia liste krawędzi na sąsiedztwa, następnie za pomocą algorytmu Dijkstry
# sprawdza najszybszą drogę do wierzchołka t, w tablicy fatigue_list trzymam jaki czas bez odpoczynku porusza się wojownik.
# złożoność czasowa to O(ElogV)


from queue import PriorityQueue
from kol2testy import runtests

def warrior(G, s, t):
  n = max(max(u, v) for u, v, _ in G) + 1
  neighbours = [[] for _ in range(n)]

  for u, v, w in G:
    neighbours[u].append((v, w))
    neighbours[v].append((u, w))

  q = PriorityQueue()
  distance = [[float("inf")] * 17 for _ in range(n)]
  distance[s][0] = 0
  q.put((0, s, 0))  # (total_time, current_node, hours_without_rest)

  while not q.empty():
    total_time, u, fatigue = q.get()

    if u == t:
      return total_time

    for v, w in neighbours[u]:
      new_fatigue = fatigue + w
      if new_fatigue > 16:
        new_fatigue = w
        new_total_time = total_time + w + 8  # Dodajemy czas odpoczynku
      else:
        new_total_time = total_time + w

      if distance[v][new_fatigue] > new_total_time:
        distance[v][new_fatigue] = new_total_time
        q.put((new_total_time, v, new_fatigue))

  return None if min(distance[t]) == float("inf") else min(distance[t])

# Zmien all_tests na True zeby uruchomic wszystkie testy
runtests(warrior, all_tests=True)


