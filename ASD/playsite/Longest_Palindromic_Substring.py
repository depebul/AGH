class Solution(object):
    def longestPalindrome(self, s):
        max_len = 1
        string = ""
        tab = [[False for i in range(len(s))] for j in range(len(s))]

        for i in range(len(s)):
            tab[i][i] = True
        for i in range(len(s)):
            for j in range(i):
                if s[i] == s[j] and (i-j <= 2 or tab[j+1][i-1]):
                    tab[j][i] = True
                    if max_len < i-j+1:
                        max_len = i-j+1
                        string = s[j:i+1]
        for i in range(len(tab)):
            print(tab[i])
        return string if string else s[0]

    s = "babad"
    print(longestPalindrome((),s))