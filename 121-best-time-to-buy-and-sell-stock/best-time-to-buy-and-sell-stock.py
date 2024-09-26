class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        m = prices[0]

        for i in range(0, len(prices)):
            profit = max(profit, prices[i] - m)
            m = min(prices[i], m)
        return profit