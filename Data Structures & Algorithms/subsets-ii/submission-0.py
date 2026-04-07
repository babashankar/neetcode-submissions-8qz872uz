class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        def dfs(path, i):
            res.append(path)

            for j in range(i, n):
                # skip duplicates at the same recursion level
                if j > i and nums[j] == nums[j - 1]:
                    continue
                dfs(path + [nums[j]], j + 1)

        dfs([], 0)
        return res
