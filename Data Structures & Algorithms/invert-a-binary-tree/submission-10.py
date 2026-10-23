# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #brute force solution 
        #recursive solution 
        #expotnetial time 

        #Base cases:
        if not root:
            return None
        
        #One node in the tree        
        else:
            tmp = root.left
            root.left = root.right
            root.right = tmp 

            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
           