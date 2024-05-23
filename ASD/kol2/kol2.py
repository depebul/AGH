# Dawid Żak, mój algorytm zamienia liste krawędzi na sąsiedztwa, następnie za pomocą algorytmu Dijkstry
# sprawdza najszybszą drogę do wierzchołka t, w tablicy fatigue_list trzymam jaki czas bez odpoczynku porusza się wojownik.
# złożoność czasowa to O(ElogV)


from kol2testy import runtests
from queue import PriorityQueue
def warrior( G, s, t):
  n = max(G, key=lambda x: x[1])[1] + 1
  neighbours = [[] for _ in range(n)]
  for i in range(len(G)):
    neighbours[G[i][0]].append([G[i][1], G[i][2]])
    neighbours[G[i][1]].append([G[i][0], G[i][2]])
  q = PriorityQueue()
  distance = [float("inf")]*(len(neighbours) + 1)
  q.put((0, s))
  distance[s] = 0
  fatigue_list = [float("inf")]*(len(neighbours) + 1)
  fatigue_list[s] = 0
  def relax(distance, v, w, u, added, new_fatigue):
    if distance[v] > distance[u] + w + added:
      distance[v] = distance[u] + w + added
      fatigue_list[v] = new_fatigue
      return True
    return False
  while not q.empty():
    dist, u = q.get()
    for v, w in neighbours[u]:
      new_fatigue = fatigue_list[u]
      added = 0
      new_fatigue += w
      if new_fatigue > 16:
        new_fatigue = 0
        added = 8
      if relax(distance, v, w, u, added,new_fatigue):
        q.put((distance[v], v))

  if distance[t] == float("inf"):
    return None
  return distance[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
