class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def scour(i,j):
            if (
                i >= len(grid) or
                j >= len(grid[0]) or
                i < 0 or
                j < 0 or
                grid[i][j] != 1
            ):
                return 0
            grid[i][j] = 0
            return 1 + scour(i+1,j) + scour(i-1,j) + scour(i,j+1) + scour(i,j-1)

        area = 0
        for i in range(0,len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    area = max(area, scour(i,j))
        return area
