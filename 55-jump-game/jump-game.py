class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gasleft = nums[0] -1

        for i in range(1, len(nums)):
            if gasleft < 0:
                return False
            gasleft = max(gasleft, nums[i])
            gasleft -= 1
        return True
