class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        c = 0
        maxC = 0
        while r < len(nums):
            if nums[r] == 0:
                c += 1
            
            while c > k:
                if nums[l] == 0:
                    c -= 1
                l += 1
            r += 1
            maxC = max(maxC, r-l)
        return maxC