from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        Inf=2147483647
        rows=len(grid)
        cols=len(grid[0])


        #store the indexes where there are treasures
        treasures=[]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    treasures.append((i,j))
        
        #start bfs from tresures in all 4 directions
        q=deque(treasures)

        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            i,j=q.popleft()

            for l,m in directions:
                #update only if the cell is land, the nearest land would already been filled with result so ignore ity
                r,x=i+l,j+m
                if 0<=r<rows and 0<=x<cols and grid[r][x]==Inf:
                    grid[r][x]=grid[i][j]+1
                    q.append((r,x))
        



        