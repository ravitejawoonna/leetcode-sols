class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        gas = 0

        for i in range(0, len(nums)):
            if gas < 0:
                return False
            gas = max(nums[i],gas)
            gas -= 1
        return True