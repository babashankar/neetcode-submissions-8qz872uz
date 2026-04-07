class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l=len(cost)
        dp=[0 for _ in range(l+1)]


        for i in range(2,l+1):
            dp[i]=min(cost[i-1]+dp[i-1],cost[i-2]+dp[i-2])
        return dp[-1]
        
        