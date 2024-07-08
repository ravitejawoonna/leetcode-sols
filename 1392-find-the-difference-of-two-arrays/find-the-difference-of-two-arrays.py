class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        ans = [[],[]]

        for a in nums1:
            if a not in nums2:
                ans[0].append(a)

        for a in nums2:
            if a not in nums1:
                ans[1].append(a)

        return ans