class Solution:
    def trap(self, height: List[int]) -> int:
        ml = [0] * len(height)
        mr = [0] * len(height)

        l_max = 0
        for i in range(0, len(height)):
            ml[i] = l_max
            l_max = max(height[i], l_max)
        
        r_max = 0
        for i in range(len(height)-1, -1, -1):
            mr[i] = r_max
            r_max = max(height[i], r_max)
        
        summ = 0

        for i in range(len(height)):
            level = min(ml[i], mr[i])
            summ += max(
                0, level-height[i]
            )
        return summ
