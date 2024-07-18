class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def feasible(capacity):
            day = 1
            total = 0
            for w in weights:
                total += w
                if total > capacity:
                    total = w
                    day += 1
                    if day > days:
                        return False
            return True
            

        while l < r:
            m = l + (r-l)//2
            if feasible(m):
                r = m
            else:
                l = m+1
        return l