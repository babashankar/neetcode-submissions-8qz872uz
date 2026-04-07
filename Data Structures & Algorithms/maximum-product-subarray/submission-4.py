class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxi=1
        mini=1
        res=max(nums)

        for i in nums:
            if maxi==0:
                maxi=1
            if mini==0:
                mini=1
            a,b=maxi,mini
            maxi=max(a*i,b*i,i)
            mini=min(a*i,b*i,i)
            res=max(res,maxi)
        return res 

        