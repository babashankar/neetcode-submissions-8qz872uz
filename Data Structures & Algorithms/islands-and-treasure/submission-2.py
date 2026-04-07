from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf=2147483647
        rows,cols=len(grid),len(grid[0])
        q=deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append((i,j,0))
        while q:
            i,j,dist=q.popleft()

            # if grid[i][j]==-1:
            #     continue
    

            if grid[i][j]==inf:
                grid[i][j]=dist
            
            directions=[(-1,0),(1,0),(0,1),(0,-1)]

            for l,m in directions:
                r,x=i+l,j+m

                if r<0 or x<0 or r==rows or x==cols:
                    continue
                if grid[r][x]!=inf:
                    continue
                q.append((r,x,dist+1))
        
            
                
            


        