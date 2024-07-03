class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = 0
        c = 0
        m_size = 0
        while r < len(nums):
            if nums[r] == 0:
                c += 1
            while c > 1:
                if nums[l] == 0:
                    c -= 1
                l += 1
            m_size = max(m_size, r-l)
            r +=1
        return m_size
                    
        