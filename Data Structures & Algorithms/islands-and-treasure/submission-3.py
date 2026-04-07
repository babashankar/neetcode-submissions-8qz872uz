from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        inf=2147483647
        rows,cols=len(grid),len(grid[0])


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append((i,j))
        directions=[(0,1),(1,0),(-1,0),(0,-1)]


        while q:
            node=q.popleft()
            i,j=node

            for x,y in directions:
                rx,ry=i+x,j+y

                if rx>=0 and ry>=0 and rx<rows and ry<cols and grid[rx][ry]==inf:
                    grid[rx][ry]=grid[i][j]+1
                    q.append((rx,ry))
        


            



        