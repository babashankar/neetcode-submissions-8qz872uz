class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        def fn(i,j):
            if i<0 or j<0 or i==rows or j==cols:
                return 0
            if grid[i][j]==0:
                return 0
            grid[i][j]=0
            res=1

            directions=[(0,1),(1,0),(-1,0),(0,-1)]
            for x,y in directions:
                res+=fn(i+x,j+y)
            return res
        res=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    
                    res=max(res,fn(i,j))
        return res      