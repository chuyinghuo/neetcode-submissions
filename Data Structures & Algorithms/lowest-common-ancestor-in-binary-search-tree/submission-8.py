# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = [root]

        def search(root):
            if not root:
                return 
            node = root
            lca[0] = node
            if node is p or node is q:
                return 
            elif node.val < p.val and node.val < q.val:
                search(node.right)
            elif node.val > p.val and node.val > q.val:
                search(node.left)
        search(root)
       
        return lca[0]
            



