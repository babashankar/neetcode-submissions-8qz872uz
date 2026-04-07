class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        def fn(i,j):
            if i<0 or j<0 or i==rows or j==cols:
                return
            if grid[i][j]=="0":
                return
            grid[i][j]="0"

            directions=[(0,1),(1,0),(-1,0),(0,-1)]
            for x,y in directions:
                fn(i+x,j+y)
        res=0


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    res+=1
                    fn(i,j)
        return res        