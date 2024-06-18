class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        tab = [[1 for _ in range(i + 1)] for i in range(rowIndex + 1)]
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                tab[i][j] = tab[i - 1][j - 1] + tab[i - 1][j]
        print(tab)
        return tab[rowIndex - 1]

    getRow((),3)