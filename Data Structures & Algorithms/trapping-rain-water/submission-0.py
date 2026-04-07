class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        right=[0 for _ in range(n)]
        currMax=float("-inf")
        for i in range(n-1,-1,-1):
            currMax=max(currMax,height[i])
            right[i]=currMax
        currMax=float("-inf")
        res=0
        for i in range(n):
            currMax=max(currMax,height[i])
            c=min(currMax,right[i])
 
            if c-height[i]>=0:
                res+=c-height[i]
        return res




        