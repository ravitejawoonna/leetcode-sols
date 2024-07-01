class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = s = float('inf')

        for i in range(0, len(nums)):
            if nums[i] <= f:
                f = nums[i]
            elif nums[i] <= s:
                s = nums[i]
            else:
                return True

        return False