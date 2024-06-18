class Solution(object):
    def climbStairs(self, n):
        tab = [-1 for _ in range(n + 1)]

        def climb(n, tab):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if tab[n] != -1:
                return tab[n]
            tab[n] = climb(n - 1, tab) + climb(n - 2, tab)
            return tab[n]
        return climb(n, tab)