class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        maxVal = -100

        while l < r:
            maxVal = max (
                min(height[l], height[r]) * (r-l),
                maxVal
            )

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxVal
