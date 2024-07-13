class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l+1, r + 1]
            if s > target:
                r -= 1
            else:
                l += 1
