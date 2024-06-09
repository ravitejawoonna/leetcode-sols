class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        ans = 1
        for i in range(1, n):
            ans = (ans + (ans * k)//i) 
        return ans % (10**9 + 7)