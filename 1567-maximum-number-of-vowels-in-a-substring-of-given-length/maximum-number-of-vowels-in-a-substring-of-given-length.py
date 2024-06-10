class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "o", "i", "u"}
        maxVal = None
        num = 0
        print(s[:k])
        for i in s[:k]:
            if i in vowels:
                num += 1

        maxVal = num

        for i in range(k, len(s)):
            print(s[i])
            if s[i] in vowels:
                num += 1
            if s[i-k] in vowels:
                num -= 1
            maxVal = max(maxVal, num)
        return maxVal