class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            num = nums[i]

            l = i+1
            r = len(nums)-1

            while l < r:
                s = num + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append(
                        [num, nums[l], nums[r]]
                    )
                    l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1                
        return res
