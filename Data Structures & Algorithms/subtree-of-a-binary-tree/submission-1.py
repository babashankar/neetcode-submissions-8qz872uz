# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def getPost(root):
            if not root:
                return "#"
            return f"{root.val},({getPost(root.left)},{getPost(root.right)})"
        return getPost(subRoot) in getPost(root)
       
        