class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        stack = [-1]

        mlen = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                idx = stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    mlen = max(
                        mlen, i-stack[-1]
                    )
        return mlen