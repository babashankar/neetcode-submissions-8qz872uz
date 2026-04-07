class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)

        res=0

        for i in nums:
            if i-1 in nums:
                continue
            d=1
            while i+1 in nums:
                d+=1
                i+=1
            res=max(res,d)
        return res        