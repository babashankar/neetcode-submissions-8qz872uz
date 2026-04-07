class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}

        def dfs(i):
            if i == n:
                return True
            if i in memo:
                return memo[i]

            for k in range(i, n):
                if s[i:k+1] in wordDict and dfs(k + 1):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)
