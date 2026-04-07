class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi,mini=1,1
        res=max(nums)

        for i in nums:
            if i==0:
                maxi,mini=1,1
            a,b=i*maxi,i*mini
            maxi=max(a,b,i)
            mini=min(a,b,i)
            res=max(res,maxi)
        return res
