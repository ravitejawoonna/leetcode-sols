class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map1 = {}

        for i in arr:
            map1[i] = map1.get(i, 0) + 1
        
        return len(list(map1.values())) == len(set(list(map1.values())))