"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        start = node
        stack = [start]
        old_to_new = {}
        visited = set()
        visited.add(start)

        while stack:
            node = stack.pop()
            old_to_new[node] = Node(val=node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
                
        for old_node, new_node in old_to_new.items():
            for n in old_node.neighbors:
                new_node.neighbors.append(old_to_new[n])
        return old_to_new[start]
                    

