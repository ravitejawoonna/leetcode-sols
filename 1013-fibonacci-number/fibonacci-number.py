class Solution:
    @cache
    def fib(self, n: int) -> int:
        # < ---- recursive 2 ^ N ---- >
        # if n < 2:
        #     return n
        # return self.fib(n-1) + self.fib(n-2)


        # < ---- Top down with memoization ---- >
        # cache = {}
        # if n < 2:
        #     return n
        # if n in cache:
        #     return cache[n]
        # cache[n] = self.fib(n-1) + self.fib(n-2)
        # return cache[n]

        # < ---- bottom up, tabulation ---- >
        if n < 2:
            return n
            
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]