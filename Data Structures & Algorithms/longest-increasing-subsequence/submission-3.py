class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l=len(nums)
        dp=[1 for _ in range(l)]
        maxi=1

        for i in range(l):
            for j in range(i+1,l):
                if nums[j]>nums[i]:
                    dp[j]=max(dp[j],dp[i]+1)
                    maxi=max(maxi,dp[j])
        
        return maxi
        