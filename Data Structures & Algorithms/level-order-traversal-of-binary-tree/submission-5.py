# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursive solution
#BFS to traverse each level of the tree 
#each level of the tree is stored within queue 
#return once there are no more nodes in the queue
#return solution as result that we are adding to with each recurisve return call
#helper bfs function 
#Runtime: O(h) for height of the tree 
#Space complexity: O(n) list we are returning

#iterative solution: use a while loop 
#runtime O(h)
#Space complexity: O(n)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #what number does the nodes in the tree range from?
        #null node append as none/null or empty?
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            curr_level = []
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    continue 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                curr_level.append(node.val)
            result.append(curr_level)
        return result
        
    




        



