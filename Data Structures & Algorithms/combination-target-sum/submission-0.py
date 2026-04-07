class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(path, remaining, i):
            if remaining == 0:
                res.append(path)
                return
            if remaining < 0 or i == n:
                return

            # option 1: skip current number
            dfs(path, remaining, i + 1)

            # option 2: take current number (stay on same index)
            dfs(path + [nums[i]], remaining - nums[i], i)

        dfs([], target, 0)
        return res
