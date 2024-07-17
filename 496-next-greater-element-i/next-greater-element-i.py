class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)

        cache = {
            n:i for i,n in enumerate(nums1)
        }

        stack = []

        for i in range(0, len(nums2)):

            while stack and stack[-1] < nums2[i]:
                item = stack.pop()
                res[cache[item]] = nums2[i]
            
            if nums2[i] in cache:
                stack.append(nums2[i])
        return res