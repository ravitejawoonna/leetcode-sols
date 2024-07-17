class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        res = [-1,-1]
        l = 0
        r = len(nums)
        while l < r:
            m = l + (r-l)//2

            if nums[m] == target:
                L = m
                while L -1 >= 0 and nums[L-1] == nums[m]:
                    L -= 1
                R = m
                while R + 1 < len(nums) and nums[R+1] == nums[m]:
                    R += 1
                return [L,R]
            
            if target <= nums[m]:
                r = m
            else:
                l = m+1
        return res
