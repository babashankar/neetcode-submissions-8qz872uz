class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp={}

        def fn(pref,i):
            if i==len(nums):
                if pref==target:
                    return 1
                return 0
            
            return fn(pref+nums[i],i+1)+fn(pref-nums[i],i+1)
        return fn(0,0)
        