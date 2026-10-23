# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSameNode(self, p, q):
        if not p and not q:
            return True  
        if p and q and p.val != q.val:
            return False 
        if not p or not q:
            return False 
        return self.isSameNode(p.left, q.left) and self.isSameNode(p.right, q.right)
 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
                
        
       
        if not root:
            return False 
        if not subRoot:
            return True
        return (self.isSameNode(root, subRoot)) or (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))

        



        


        