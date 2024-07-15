class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours_to_eat = 0
            for p in piles:
                hours_to_eat += math.ceil(p/k)
            return hours_to_eat <= h
        

        r = max(piles)
        l=1

        while l < r:
            m = l + (r-l) // 2
            if k_works(m):
                r = m
            else:
                l = m+1
        return l
