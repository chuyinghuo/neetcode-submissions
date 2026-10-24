# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #initalize deque
        q = deque([root])

        res = []
        #edge case
        if not root:
            return []
        #bfs 
        while q:
            current_level = []
            for _ in range(len(q)):
                node = q.popleft()
             #   if not node:
                #    continue 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                current_level.append(node.val)
            res.append(current_level)
        return res
            

