class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        m = 0

        while l < r:
            area = (r-l) * min(height[l], height[r])
            m = max(m, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return m