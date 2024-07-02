class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        while l < len(nums) and nums[l] != 0:
            l += 1

        s = l
        for j in range(s, len(nums)):
            if nums[j]:
                nums[l], nums[j] = nums[j], nums[l]
                l += 1

        return nums