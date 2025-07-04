class Solution(object):
    def generate(self, numRows):
        # that was my solution
        tab = [[1 for _ in range(i + 1)] for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                tab[i][j] = tab[i - 1][j - 1] + tab[i - 1][j]
        return tab

