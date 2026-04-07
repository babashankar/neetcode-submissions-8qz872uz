class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,ele in enumerate(nums):
            if target-ele in d:
                return [d[target-ele],i]
            d[ele]=i
            


        