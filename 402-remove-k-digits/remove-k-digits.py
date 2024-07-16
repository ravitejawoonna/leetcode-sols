class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        at = k
        for i in range(0, len(num)):
            if not stack:
                stack.append(int(num[i]))
                continue
            
            while stack and at > 0 and stack[-1] > int(num[i]):
                stack.pop()
                at -=1
            stack.append(int(num[i]))
        
        if at != 0:
            stack = stack[:-at]

        if len(stack) == 0:
            return "0"
        print(stack)
        r = "".join([str(i) for i in stack]).lstrip("0") 
        if len(r) == 0:
            return "0"
        return r