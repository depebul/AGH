class Solution(object):
    def jump(self, nums):
        n = len(nums)
        tab = [[float("inf") for _ in range(n)] for _ in range(n)]
        tab[0][0] = 0
        for i in range(1,n):
            for j in range(i, n):
                tab[i][j] = min(tab[i-1][j],tab[i][j])
                if j > n:
                    print("dlugosc")
                    break
                if j > nums[i-1] + i-1:
                    print("skok")
                    continue
                tab[i][j] = min(tab[i][j], tab[i-1][i-1] + 1)
        return tab[n-1][n-1]