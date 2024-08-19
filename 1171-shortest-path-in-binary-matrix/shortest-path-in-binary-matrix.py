class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direct = [
            [1,0], [0,1], [-1,0], [0,-1],
            [1,1], [-1,-1], [-1, 1], [1,-1] 
        ]
        visited = set()
        q = deque(
            [(0,0,1)]
        )
        N = len(grid)

        while q:
            r,c,length = q.popleft()

            if min(r,c) < 0 or max(r,c) >= len(grid) or grid[r][c] == 1:
                continue
            
            if r == N-1 and c == N-1:
                return length
            
            for dr, dc in direct:
                if (r + dr, c + dc) not in visited:
                    q.append(
                        [r+dr, c+dc, length + 1]
                    )
                    visited.add(
                        (r+dr, c+dc)
                    )
        return -1