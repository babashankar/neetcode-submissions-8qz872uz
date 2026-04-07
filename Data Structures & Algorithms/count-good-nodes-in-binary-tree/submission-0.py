

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root,maxi):
            if not root:
                return 0
            if root.val>=maxi:
                return 1+helper(root.left,root.val)+helper(root.right,root.val)
            return helper(root.left,maxi)+helper(root.right,maxi)
        return helper(root,float("-inf"))
            
        
            
            
        