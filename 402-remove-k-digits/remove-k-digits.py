class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        at = k

        for i in range(0, len(num)):
            if not stack:
                stack.append(num[i])
                continue
            
            while at > 0 and stack and int(stack[-1]) > int(num[i]):
                stack.pop()
                at -= 1
            
            stack.append(num[i])
        
        if at != 0:
            stack = stack[:-at]
        return "".join(stack).lstrip("0") or "0"