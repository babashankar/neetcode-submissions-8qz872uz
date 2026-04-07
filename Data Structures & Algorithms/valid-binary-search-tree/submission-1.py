# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,start,end):
            if not root:
                return True
            if root.val>start and root.val<end:
                return dfs(root.left,start,root.val) and dfs(root.right,root.val,end)
            return False
        return dfs(root,float("-inf"),float("inf"))
            
        