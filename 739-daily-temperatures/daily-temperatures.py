class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []
        res = [0] * len(t)

        for i in range(0, len(t)):
            # stack -> [temp, idx]
            while stack and stack[-1][0] < t[i]:
                item = stack.pop()
                res[item[1]] = i - item[1]
            
            stack.append([t[i], i])
        return res