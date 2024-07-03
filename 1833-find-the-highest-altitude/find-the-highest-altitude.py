class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        p_sum = 0
        maxP = 0
        for i in range(len(gain)):
            p_sum = p_sum + gain[i]
            maxP = max(maxP, p_sum)
        return maxP