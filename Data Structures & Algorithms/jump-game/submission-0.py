class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump=0
        l=len(nums)

        for i in range(l):
            if maxJump>=l-1:
                return True
            if maxJump<i:
                return False
            maxJump=max(maxJump,i+nums[i])
        return True

        