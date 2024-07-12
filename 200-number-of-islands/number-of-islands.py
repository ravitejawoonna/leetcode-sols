class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def rec(i,j):
            if (
                i < 0 or
                j < 0 or
                i >= len(grid) or
                j >= len(grid[0]) or
                grid[i][j] != "1"
            ):
                
                return
                
            grid[i][j] = "#"
            rec(i+1, j)
            rec(i-1, j)
            rec(i,j+1)
            rec(i,j-1)

        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1":
                    rec(i,j)
                    count += 1
        return count           