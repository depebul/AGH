from egz3btesty import runtests

def uncool( P ):
  n = len(P)
  P = [(P[i][0], P[i][1], i) for i in range(n)]
  for s1, s2 in (1, 1), (-1, 1), (1, -1), (-1, -1):
    for i1, i2 in (0, 1), (1, 0):
      P.sort(key=lambda x: (s1 * x[i1], s2 * x[i2]))
      for i in range(1, n):
        a, b, j = P[i - 1]
        c, d, k = P[i]
        if a < c < b and c < b < d:
          return j, k
  return None
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = False )
