class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        l=len(nums)
        if l==1:
            return nums[0]
        maxi=float("-inf")
        for i in range(l):
            a,b,c=1,nums[i],1
            if i-1>=0:
                a=nums[i-1]
            if i+1<l:
                c=nums[i+1]
            maxi=max(maxi,a*b*c+self.maxCoins(nums[:i]+nums[i+1:]))
        return maxi
            



        