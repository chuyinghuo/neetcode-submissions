
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        lca = [root]

        def search(root):
            if not root:
                return 
            lca[0] = root
           
            if root is p or root is q:
                return 
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            elif root.val > p.val and root.val > q.val:
                search(root.left)
            else:
                return 
        search(root)
        return lca[0]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#edge cases: not root, not p or not q 
#if not p and not q, return root 
#brute force: iterate through every single node in the tree, and find the node with the least depth. Time complexity: O(n) approach where n is the number of nodes in the tree. Space complexity O(1), auxillary variables 

#optimal solution: 
#iterative preorder traveral on dfs
#initalize a stack = [root]
#while loop which contuines while the stack is not null 
#append each node along a dfs path of p and q onto the stack 
#initalize a global variable like lowest outside of the loop which we update when we have found a lower common ancestor. We would check if the new node is a lower common ancestor by the depth of that new node. 
#create a helper function to determine the depth of the node 
#return the global lowest common ancestor variable 
#Time: O(height of the tree)
#Space: O(1) based on auxillary variables
