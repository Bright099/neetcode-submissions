from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board [i][j] == '.':
                    continue
                if board[i][j] not in rows[i]:
                    rows[i].add(board[i][j])
                else:
                    return False
                
                if board[i][j] not in columns[j]:
                    columns[j].add(board[i][j])
                else:
                    return False

                if board[i][j] not in squares[i//3, j//3]:
                    squares[i//3, j//3].add(board[i][j])
                else:
                    return False
        return True
        