class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        l, r = 0, len(nums)-1

        while l < r:
            mid = l + (r-l)//2
            if nums[mid] >= target :
                if nums[mid] == target:
                    return mid
                r = mid
            else:
                l = mid + 1
        return l