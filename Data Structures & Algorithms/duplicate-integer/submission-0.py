class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        di={}
        for i in nums:
            if i in di:
                return True
            di[i]=True
        return False
        