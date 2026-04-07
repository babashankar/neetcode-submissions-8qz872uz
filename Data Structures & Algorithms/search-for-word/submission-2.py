class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordLen=len(word)
        rows,cols=len(board),len(board[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]


        def fn(i,j,k):
            if k==wordLen:
                return True
            if i<0 or j<0 or i==rows or j==cols:
                return False
            if board[i][j]=="#":
                return False
            if board[i][j]==word[k]:
                tmp=board[i][j]
                board[i][j]="#"
                for a,b in directions:
                    r,x=i+a,j+b
                    if fn(r,x,k+1):
                        return True
                board[i][j]=tmp
            return False
        for i in range(rows):
            for j in range(cols):
                if fn(i,j,0):
                    return True
        return False

            
    
        