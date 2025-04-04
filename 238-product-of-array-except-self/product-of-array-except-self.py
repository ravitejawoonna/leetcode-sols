class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        pre = [1] * len(nums)
        for i in range(len(nums)):
            pre[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        pos = [1] * len(nums)
        for i in range(len(nums) -1,-1,-1):
            pos[i] = postfix
            postfix *= nums[i]
        
        for i in range(len(nums)):
            res[i] = pre[i] * pos[i]
        return res