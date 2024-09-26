class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cache = defaultdict(int)

        for i in text:
            cache[i] = cache.get(i, 0) + 1

        return min(
            cache.get("b", 0),
            cache.get("a", 0),
            cache.get("l", 0) // 2,
            cache.get("o", 0) // 2,
            cache.get("n", 0)
        )