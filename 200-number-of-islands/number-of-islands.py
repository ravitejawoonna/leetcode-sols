class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])

        def scout(i,j):
            if (
                i < 0 or
                i >= len(grid) or
                j < 0 or
                j >= len(grid[0]) or
                grid[i][j] != "1"
            ):
                return 

            grid[i][j] = "#"
            scout(i+1,j)
            scout(i-1, j)
            scout(i, j+1)
            scout(i, j-1)
        
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == "1":
                    count += 1
                    scout(i,j)
        return count            