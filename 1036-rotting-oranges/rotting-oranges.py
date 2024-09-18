class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        fresh = set()
        rotten = []

        for i in range(0, R):
            for j in range(0, C):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    rotten.append((i,j))
        

        def rotIdx(i,j):
            if (
                i < 0 or j < 0 or
                i >= R or j >= C or
                grid[i][j] != 1
            ):
                return None
            if (i,j) in fresh:
                fresh.remove((i,j))

            grid[i][j] = 2
            return (i,j)
            
        minutes = 0
        while len(rotten):
            new_rotten = []
            for r in rotten:
                i,j = r[0], r[1]
                new_rotten = new_rotten + list(filter(lambda x: x is not None, [
                    rotIdx(i+1,j),
                    rotIdx(i-1,j),
                    rotIdx(i,j+1),
                    rotIdx(i,j-1)
                ]))
            if len(new_rotten):
                minutes += 1
            rotten = new_rotten
        
        if len(fresh) == 0:
            return minutes
        else:
            return -1