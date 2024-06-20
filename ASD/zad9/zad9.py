from zad9testy import runtests

def trip(M):
  m, n = len(M), len(M[0])
  dp = [[-1]*n for _ in range(m)]
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  def dfs(i, j):
    if dp[i][j] != -1:
      return dp[i][j]
    dp[i][j] = 1
    for dx, dy in directions:
      x, y = i + dx, j + dy
      if 0 <= x < m and 0 <= y < n and M[x][y] > M[i][j]:
        dp[i][j] = max(dp[i][j], 1 + dfs(x, y))
    return dp[i][j]
  return max(dfs(i, j) for i in range(m) for j in range(n))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )
