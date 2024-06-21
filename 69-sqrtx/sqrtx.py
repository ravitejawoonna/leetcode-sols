class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        l , r = 1, x

        while l < r:
            mid = l + (r-l)//2
            if  mid * mid > x:
                r = mid
            else:
                l = mid + 1
        return l - 1