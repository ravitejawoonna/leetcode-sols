class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs = 0

        store = {}

        for i in range(0, len(nums)):
            diff = k - nums[i]
            if nums[i] in store and store[nums[i]] > 0:
                pairs += 1
                store[nums[i]] -= 1
            else:
                store[diff] = store.get(diff, 0) + 1
        return pairs