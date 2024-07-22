class Solution:
    def frequencySort(self, s: str) -> str:
        cache = {}
        for i in s:
            cache[i] = cache.get(i, 0) + 1
        arr = [
            (-c, i) for i,c in cache.items()
        ]

        heapq.heapify(arr)
        res = ""
        for _ in range(len(arr)):
            item = heapq.heappop(arr)
            res = res + "".join([item[1] for _ in range(-1 * item[0])])
        return res