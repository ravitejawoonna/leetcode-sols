class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return 1
        stones = list(map(lambda x: -1 * x, stones))
        heapq.heapify(stones)

        while len(stones) > 1:
            one, two = -1 * heapq.heappop(stones), -1 * heapq.heappop(stones)
            diff = one - two
            if diff:
                heapq.heappush(stones, -1 * diff)
        
        return -1 * stones[-1] if len(stones) else 0