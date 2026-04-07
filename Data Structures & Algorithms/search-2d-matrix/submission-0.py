class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])

        l=0

        r=rows*cols-1

        while l<=r:
            mid=(l+r)//2

            row,col=mid//cols,mid%cols
            a=matrix[row][col]
            if a==target:
                return True
            if target>a:
                l=mid+1
            else:
                r=mid-1
            
        return False
        