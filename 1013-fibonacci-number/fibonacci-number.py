class Solution:
    @cache
    def fib(self, n: int) -> int:
        # < ---- recursive 2 ^ N ---- >
        # if n < 2:
        #     return n
        # return self.fib(n-1) + self.fib(n-2)


        # < ---- Top down with memoization ---- >
        cache = {}
        if n < 2:
            return n
        if n in cache:
            return cache[n]
        cache[n] = self.fib(n-1) + self.fib(n-2)
        return cache[n]