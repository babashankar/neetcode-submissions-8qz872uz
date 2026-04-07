class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        l = len(word)

        def dfs(ind, i, j):
            if ind == l:
                return True

            if i < 0 or j < 0 or i == rows or j == cols:
                return False

            if board[i][j] != word[ind]:
                return False

            # mark visited
            temp = board[i][j]
            board[i][j] = "#"

            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                if dfs(ind + 1, i + dx, j + dy):
                    return True

            # backtrack
            board[i][j] = temp
            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(0, i, j):
                    return True

        return False
