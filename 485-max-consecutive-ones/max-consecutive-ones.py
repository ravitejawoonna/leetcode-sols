class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxc = c = 0

        for i in nums:
            if i:
                c += 1
                maxc = max(c, maxc)
            else:
                c = 0
        return maxc