class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVol = -100

        l, r = 0, len(height) - 1

        while l < r:
            maxVol = max(
                maxVol,
                min(height[l], height[r]) * (r-l)
            )

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return maxVol