class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # [min, maxVal]
        curr_min = nums[0]

        for n in nums[1:]:
            # we are looping to find the mid element
            while stack and n >= stack[-1][0]:
                # popping all the element[0] greater than current element
                stack.pop()

            if stack and n > stack[-1][1]:
                return True

            stack.append([n, curr_min]) # storing [max, min] hoping to find the pattern
            curr_min = min(n, curr_min)        
        return False    
