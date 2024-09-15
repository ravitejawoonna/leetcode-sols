class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # < ---- Recursive, Brute force ----- >
        # @cache
        # def rec(i,j):
        #     if i >= m or j >= n:
        #         return 0
        #     if i == m-1 and j == n-1:
        #         return 1
            
        #     res = rec(i+1,j) + rec(i,j+1)
        #     return res
        # return rec(0,0)

        # top down
        dp = [
            [0 for _ in range(n)] for _ in range(m)
        ]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j-1]
        return dp[-1][-1]

        