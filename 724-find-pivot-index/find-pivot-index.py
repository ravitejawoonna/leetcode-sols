class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = [0] * len(nums)
        pos = [0] * len(nums)

        s = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            pos[i] = s
            s += nums[i]
        
        s = nums[0]
        for i in range(1, len(nums)):
            pre[i] = s
            s += nums[i]

        for i in range(0, len(nums)):
            if pre[i] == pos[i]:
                return i
        return -1