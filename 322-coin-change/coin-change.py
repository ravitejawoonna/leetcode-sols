class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # < ---- brute force ----- >
        # @cache
        # def rec(s, n):
        #     if s > amount:
        #         return math.inf

        #     if s == amount:
        #         return n

        #     return min(
        #         [
        #             rec(s+i, n+1) for i in coins
        #         ]
        #     )
        # res = rec(0,0)
        # return -1 if res == math.inf else res

        # < ---- Bottom up tabuliztion ---- >
        dp = [0] * (amount + 1)

        coins.sort()
        # finding the minimum number of coins required for all amounts up until amount

        for i in range(1, amount+1):
            minn = float('inf')
            for c in coins:
                diff = i - c
                if diff < 0:
                    break
                minn = min(
                    minn, dp[diff]+1
                )
            dp[i] = minn
        print(dp)
        if dp[amount] < float('inf'):
            return dp[amount]
        return -1