class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxIdx = None
        maxVal = -100
        res = [True] * len(candies)
        for i in range(0, len(candies)):
            if candies[i] > maxVal:
                maxVal = candies[i]
                maxIdx = i

            if candies[i] + extraCandies < maxVal:
                res[i] = False
        
        for i in range(0, maxIdx):
            if candies[i] + extraCandies < maxVal:
                res[i] = False
        return res

        