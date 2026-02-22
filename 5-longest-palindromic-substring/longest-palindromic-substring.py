class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen, resId = 0, 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1): 
            for j in range(i, n): 
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]): 
                    dp[i][j] = True 
                    if resLen < j - i + 1: 
                        resLen = j - i + 1 
                        resId = i 

        return s[resId : resId + resLen]


        