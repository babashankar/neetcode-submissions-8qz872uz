# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
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
        while res and res[-1]=="null":
            res.pop()
        return ",".join(res)
            



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes=data.split(",")
        if not nodes or nodes[0]=="null":
            return None

        root=TreeNode(nodes[0])

        q=deque([root])
        i=1
        n=len(nodes)

        while q:
            node=q.popleft()
            if i<n and nodes[i]!="null":
                l=TreeNode(int(nodes[i]))
                node.left=l
                q.append(l)
            i+=1
            if i<n and nodes[i]!="null":
                r=TreeNode(int(nodes[i]))
                node.right=r
                q.append(r)
            i+=1
        return root


