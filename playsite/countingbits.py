class Solution(object):
    def countBits(self, n):
        tab = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            tab[i] = tab[i >> 1] + (i & 1)
        return tab