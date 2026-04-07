class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        dp={}
        def fn(i,j):
            if i>=l:
                return 0
            p=(i,j)
            if p in dp:
                return dp[p]
            if j:
                m= max(0-prices[i]+fn(i+1,not j),fn(i+1, j))
            else:
                m=max(0+prices[i]+fn(i+2,not j),fn(i+1, j))
            dp[p]=m
            return m
        return fn(0,True)
        