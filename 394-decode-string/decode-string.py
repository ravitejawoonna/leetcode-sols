class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(0, len(s)):
            if s[i] != "]":
                if not stack:
                    stack.append(s[i])
                    continue
                else:
                    if (stack[-1].isdigit() and s[i].isdigit()) or (stack[-1].isalpha() and s[i].isalpha()):
                        stack[-1] = stack[-1] + s[i]
                        continue
                    stack.append(s[i])
            else:
                rep_str = ""
                while stack[-1] != "[":
                    rep_str = stack.pop() + rep_str
                stack.pop() # [
                times = stack.pop()
                stack.append(
                    "".join([rep_str for _ in range(int(times))])
                )
        return "".join(stack)