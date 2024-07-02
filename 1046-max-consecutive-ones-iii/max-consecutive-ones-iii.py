class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        c = 0
        maxc = 0
        while r < len(nums):
            if not nums[r]:
                c += 1
            while c > k:
                if not nums[l]:
                    c -= 1
                l += 1
            r += 1
            maxc = max(maxc, r-l)
        return maxc