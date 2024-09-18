class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(
            r, c, visited, prevHeight
        ):
            if (
                r < 0 or c < 0 or
                r >= R or c >= C or
                heights[r][c] < prevHeight or 
                (r,c) in visited
            ):
                return
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])

        for c in range(C):
            dfs(0,c,pac,heights[0][c])
            dfs(R-1,c,atl,heights[R-1][c])

        for r in range(R):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, C-1, atl, heights[r][C-1])

        res = []

        for i in range(R):
            for j in range(C):
                if (i,j) in atl and (i,j) in pac:
                    res.append([i,j])
        return res