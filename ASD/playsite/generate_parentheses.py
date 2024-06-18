class Solution(object):
    def generateParenthesis(self, n):
        self.countin = 0
        tab = []
        def generate(left, right,p=""):
            if right == 0:
                tab.append(p)
                return
            if left > 0:
                generate(left-1, right,p + "(")
            if right > left:
                generate(left, right-1,p + ")")
        generate(n, n)
        return tab
s = Solution()
print(s.generateParenthesis(3))