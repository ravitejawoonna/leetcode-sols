class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # circular - do nums1 + nums1 to emulate circular

        stack = []
        res = [-1] * len(nums)
        for i in list(range(len(nums))) * 2:
            if not stack:
                stack.append(i)
                continue
            
            while stack and nums[stack[-1]] < nums[i]:
                item = stack.pop()
                res[item] = nums[i]
            
            stack.append(i)

        return res
