class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        post=[1 for _ in range(l)]
        post[-1]=nums[-1]

        for i in range(l-2,-1,-1):
            post[i]=nums[i]*post[i+1]
        
        pref=1
        post.append(1)
        res=[]
        for i in range(l):
            res.append(pref*post[i+1])
            pref=pref*nums[i]
        return res
        