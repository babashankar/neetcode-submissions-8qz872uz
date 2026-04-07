# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = righ
from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q=deque([root])
        res=[]

        while q:
            node=q.popleft()
            if not node:
                res.append("null")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data)==0:
            return None
        nodes=list(data.split(","))

        root=TreeNode(data[0])
        q=deque([root])

        i=1
        while q and i<len(data):
            node=q.popleft()
            if nodes[i]!="null":
                a=TreeNode(int(nodes[i]))
                node.left=a
                q.append(a)
            i+=1
            if nodes[i]!="null":
                a=TreeNode(int(nodes[i]))
                node.right=a
                q.append(a)
            i+=1
        return root

