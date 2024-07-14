class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort based on length
        strs = sorted(strs, key = lambda k: len(k))
        prefix = strs[0]

        for i in range(len(strs[0]), -1, -1):
            if all(
                [prefix[:i] == x[:i] for x in strs]
            ):
                return prefix[:i]
        return ""