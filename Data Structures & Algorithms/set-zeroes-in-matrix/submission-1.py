class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m=len(matrix)
        n=len(matrix[0])

        isZero=False

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    if j>0:
                        matrix[0][j]=0
                    else:
                        isZero=True
                    
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if matrix[0][0]==0:
            for i in range(n):
                matrix[0][i]=0
        if isZero:
            for j in range(m):
                matrix[j][0]=0
        


        
        