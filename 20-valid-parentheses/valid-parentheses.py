class Solution:
    def isValid(self, s: str) -> bool:
        openp = "{(["
        pairs = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        stack = []

        for i in range(0, len(s)):
            if s[i] in openp:
                stack.append(s[i])
                continue
            else:
                if not stack:
                    return False
                if pairs[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        return not len(stack)