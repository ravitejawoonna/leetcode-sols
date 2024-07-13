class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0 
        for item in nums:
            if item-1 in nums:
                continue
            else:
                temp = 1
                while item + 1 in nums:
                    temp += 1
                    item += 1
                count = max(temp, count)
        return count