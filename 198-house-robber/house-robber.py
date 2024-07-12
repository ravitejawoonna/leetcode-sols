class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[1], nums[0])

        dp = [nums[0], max(nums[0], nums[1])] + [0] * (len(nums)-2)

        for i in range(2, len(dp)):
            dp[i] = max(
                dp[i-2] + nums[i],
                dp[i-1]
            ) 
        return max(dp[-1], dp[-2])
