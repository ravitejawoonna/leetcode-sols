class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [-float('inf')]*(len(nums)+1)
        dp[1] = nums[0]
        maxSubSeq = 1
        for i in range(1,len(nums)):
            for j in range(maxSubSeq,0,-1):
                if nums[i] > dp[j]:
                    dp[j+1] = nums[i]
                    maxSubSeq = max(j+1,maxSubSeq)
                    break
                elif nums[i] < dp[j] and j==1:
                    dp[1] = nums[i]
        
        return maxSubSeq
            