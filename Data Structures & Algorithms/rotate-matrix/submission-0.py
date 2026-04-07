class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)

        def reverse(ind):
            l=0
            r=n-1
            while l<r:
                matrix[i][l],matrix[i][r]=matrix[i][r],matrix[i][l]
                l+=1
                r-=1

        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            reverse(i)
            
        
                