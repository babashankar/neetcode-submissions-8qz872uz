# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res=0


        def pre(root,gt):
            if not root:
                return
            gt=max(root.val,gt)

            if root.val==gt:
                self.res+=1
            pre(root.left,gt)
            pre(root.right,gt)
        pre(root,float("-inf"))
        return self.res
            
            
        