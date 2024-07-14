class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1  
        start = 0
        tot = 0

        for i in range(0, len(gas)):

            diff = gas[i] - cost[i]
            tot += diff

            if tot < 0:
                start = i+ 1
                tot = 0
        return start