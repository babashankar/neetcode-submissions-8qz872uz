class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        res=0
        for n in nums:
            if (n-1) not in numset:
                l=0
                while n+l in numset:
                    l+=1
                res=max(res,l)
        return res
        


            
        