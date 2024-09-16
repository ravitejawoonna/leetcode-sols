class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        m = 1
        for i in range(0, len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(
                        dp[j] + 1,
                        dp[i]
                    )
                    m = max(dp[i], m)
        return m