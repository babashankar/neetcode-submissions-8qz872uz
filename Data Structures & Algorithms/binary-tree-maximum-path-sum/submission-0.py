# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res=float("-inf")
        def helper(root):
            if not root:
                return 0
            l=max(helper(root.left),0)
            r=max(helper(root.right),0)
            self.res=max(self.res,root.val+l+r)
            return root.val+max(l,r)
        d=helper(root)
        return max(d,self.res)
        