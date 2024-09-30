class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            m = (l+r)//2

            if nums[m] >= target:
                if target == nums[m]:
                    return m
                r = m
            else:
                l = m + 1
        return l