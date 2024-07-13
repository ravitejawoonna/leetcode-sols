class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in cache:
                return [i, cache[diff]]
            else:
                cache[nums[i]] = i