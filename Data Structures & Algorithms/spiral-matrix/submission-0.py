class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        rows,cols=len(matrix),len(matrix[0])



        t=0
        b=rows-1
        l=0
        r=cols-1

        while l<=r and t<=b:
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t+=1

            for i in range(t,b+1):
                res.append(matrix[i][r])
            r-=1

            if l>r or t>b:
                break

            for i in range(r,l-1,-1):
                res.append(matrix[b][i]) 
            b-=1

            for i in range(b,t-1,-1):
                res.append(matrix[i][l])  

            l+=1
        return res
                 