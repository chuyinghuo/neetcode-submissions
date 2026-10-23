# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #recursive solution, could be optimized even furthur for iterative solution
        #come back for iterative solution 
        lca = [root]

        def search(root):
            lca[0] = root
            if not root:
                return 
            if root is p or root is q:
                return 
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            elif root.val > p.val and root.val > q.val:
                search(root.left)
        search(root)
        return lca[0]
