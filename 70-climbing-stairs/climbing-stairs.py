class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def rec(n):
            if n <= 0: return 0
            if n == 1: return 1
            if n == 2: return 2

            res = rec(n-1) + rec(n-2)
            return res
        
        return rec(n)