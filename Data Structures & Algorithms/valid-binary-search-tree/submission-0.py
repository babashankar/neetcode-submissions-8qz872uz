# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        def validate(root,leftMax,rightMax):
            if not root:
                return True
            if leftMax<root.val<rightMax:
                return validate(root.left,leftMax,root.val) and validate(root.right,root.val,rightMax)
            return False
        return validate(root,float("-inf"),float("inf"))
