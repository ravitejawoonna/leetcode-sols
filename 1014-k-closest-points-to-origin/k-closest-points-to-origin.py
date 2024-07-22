class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hh = []

        for i in points:
            hh.append(
                ((i[0] * i[0] + i[1] * i[1]), i)
            )
        
        heapq.heapify(hh)
        res = []
        for i in range(k):
            res.append(heapq.heappop(hh)[1])
        return res