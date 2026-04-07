class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pac = set()
        atl = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visited, prev_height):
            if ((r, c) in visited or 
                r < 0 or c < 0 or r >= rows or c >= cols or
                heights[r][c] < prev_height):
                return

            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Pacific (top and left)
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])

        # Atlantic (bottom and right)
        for c in range(cols):
            dfs(rows-1, c, atl, heights[rows-1][c])
        for r in range(rows):
            dfs(r, cols-1, atl, heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
