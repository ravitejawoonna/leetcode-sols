class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        vals = [1 for _ in range(n)]

        for _ in range(k):
            for i in range(1, n):
                vals[i] = vals[i] + vals[i-1]
        return vals[-1] % 1000000007