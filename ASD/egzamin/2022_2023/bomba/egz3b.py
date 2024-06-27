from egz3btesty import runtests

def uncool(P):
  n = len(P)
  for i in range(n):
    for j in range(i + 1, n):
      a, b = P[i]
      c, d = P[j]
      # Sprawdzanie czy przedziały są rozłączne
      if b < c or d < a:
        continue
      # Sprawdzanie czy któryś z przedziałów zawiera się w drugim
      if (a <= c and b >= d) or (c <= a and d >= b):
        continue
      # Jeśli nie są ani rozłączne ani nie zawierają się wzajemnie, są niefajne
      return (i, j)
  return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )
