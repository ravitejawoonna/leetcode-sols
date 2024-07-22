class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = [
            (-1 * heights[i], names[i]) for i in range(len(heights))
        ]

        heapq.heapify(arr)
        res = []

        for _ in range(len(heights)):
            item = heapq.heappop(arr)
            res.append(item[1])
        return res