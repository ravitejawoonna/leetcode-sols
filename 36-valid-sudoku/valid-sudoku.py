class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                if ("r", i, board[i][j]) in seen:
                    return False
                else:
                    seen.add(
                        ("r", i, board[i][j]) 
                    )
                
                if ("c", j, board[i][j]) in seen:
                    return False
                else:
                    seen.add(
                        ("c", j, board[i][j]) 
                    )
                
                if ("b", (i//3, j//3), board[i][j]) in seen:
                    return False
                else:
                    seen.add(
                        ("b", (i//3, j//3), board[i][j])
                    )
        return True