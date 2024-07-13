class Solution:
    def coinChange(self, coins, amount):
        
        @lru_cache(maxsize=None)  
        def dfs(curr):
            if curr > amount: 
                return math.inf
            if curr == amount: 
                return 0
            return min(dfs(curr + val) + 1 for val in coins)
                
        result = dfs(0)
        
        return -1 if result == math.inf else result