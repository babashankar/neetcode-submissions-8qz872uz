class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l=len(nums)
        res=[]
        def fun(prefList,remaining):
            if len(prefList)==l:
                res.append(prefList)
            for i in range(len(remaining)):
                fun(prefList+[remaining[i]],remaining[:i]+remaining[i+1:])
        fun([],nums)
        return res

        