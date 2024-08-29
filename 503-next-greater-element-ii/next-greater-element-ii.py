class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [] 
        res = [-1 for _ in range(0, len(nums))]

        for i in list(range(len(nums))) * 2:

            while stack and stack[-1][0] < nums[i]:
                item = stack.pop()
                res[item[1]] = nums[i]
                 

            stack.append(
                [nums[i], i]
            )
        return res