class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = ""
        s_len = float('inf')
        for s in strs:
            if s_len > len(s):
                s_len = len(s)
                shortest = s
            
        if len(shortest) == 0:
            return ""
        
        for i in range(s_len, -1, -1):
            if all(
                [
                    shortest[:i] == x[:i] for x in strs
                ]
            ):
                return shortest[:i]
        return ""