class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = [[] for _ in range(len(nums) + 1)]
        cache = {}

        for num in nums:
           cache[num] = cache.get(num, 0) + 1
        
        for key, val in cache.items():
            store[val].append(key)
        
        res = []
        for i in range(len(store)-1,-1,-1):
            for j in store[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res