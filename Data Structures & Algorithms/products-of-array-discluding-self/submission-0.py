class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1 for _ in range(len(nums)+2)]
        postfix=[1 for _ in range(len(nums)+2)]
        for i in range(len(nums)):
            prefix[i]=nums[i]*prefix[i-1]
        for i in range(len(nums)-1,-1,-1):
            postfix[i]=nums[i]*postfix[i+1]
        res=[]
        for i in range(len(nums)):
            res.append(prefix[i-1]*postfix[i+1])
        return res
        

        