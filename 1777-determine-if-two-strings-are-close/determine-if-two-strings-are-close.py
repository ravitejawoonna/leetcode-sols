class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ch1 = [0] * 26
        ch2 = [0] * 26

        if len(word1) != len(word2):
            return False

        for i in range(0, len(word1)):
            ch1[ord(word1[i]) - ord('a')] += 1
            ch2[ord(word2[i]) - ord('a')] += 1

        for i in range(26):
            if ch1[i] == 0 and ch2[i] != 0 or ch2[i] == 0 and ch1[i] != 0:
                return False

        ch1.sort()
        ch2.sort()

        if ch1 == ch2:
            return True

        return False