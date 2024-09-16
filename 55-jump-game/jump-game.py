class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gasleft = 0

        for i in range(0, len(nums)):
            if gasleft < 0:
                return False
            gasleft = max(nums[i], gasleft)
            gasleft -= 1
        return True