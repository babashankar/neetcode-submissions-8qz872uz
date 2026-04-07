class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns=defaultdict(list)
        rows=defaultdict(list)
        grids=defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in grids[(i//3,j//3)]:
                    return False
                print("hello")
                rows[i].append(board[i][j])
                columns[j].append(board[i][j])
                grids[(i//3,j//3)].append(board[i][j])
        return True
        