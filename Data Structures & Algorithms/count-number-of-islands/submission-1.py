class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])

        def dfs(i,j):
            if i<0 or j<0 or i==rows or j==cols:
                return
            if grid[i][j]=="0":
                return
            directions=[(0,1),(1,0),(-1,0),(0,-1)]

            grid[i][j]="0"

            for l,m in directions:
                dfs(i+l,j+m)
        res=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    res+=1
                    dfs(i,j)
        return res



