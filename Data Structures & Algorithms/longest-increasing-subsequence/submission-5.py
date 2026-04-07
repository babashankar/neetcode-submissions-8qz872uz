class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l=len(nums)
        res=[1 for _ in range(l)]

        for i in range(l):
            for j in range(i+1,l):
                if nums[j]>nums[i]:
                    res[j]=max(res[j],res[i]+1)
        return max(res)
        