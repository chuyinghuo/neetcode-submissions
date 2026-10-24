# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #using the properties of a bst, build a sorted list
        #1-index into the kth element of this array 


        #brute force, iterate through every single node, built a list of integers, sort, return the kth element of the array 

        #use bfs or dfs 

        stack = []
        curr = root
        count = 0 

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left 
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right 
        





         

