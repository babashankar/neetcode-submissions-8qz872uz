class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols=len(board),len(board[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols:
                return 
            if board[i][j] in ["X","T"]:
                return
            board[i][j]="T"
            directions=[(0,1),(0,-1),(1,0),(-1,0)]
            for l,m in directions:
                r,x=l+i,j+m
                dfs(r,x)
        for j in range(cols):
            dfs(0,j)
            dfs(rows-1,j)
        for i in range(rows):
            dfs(i,0)
            dfs(i,cols-1)
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="T":
                    board[i][j]="O"
                else:
                    board[i][j]="X"
        
        