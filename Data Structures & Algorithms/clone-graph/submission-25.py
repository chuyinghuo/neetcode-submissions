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
        visited = set()
        old_to_new = {}
        stack = [start]
        visited.add(start)

        while stack:
            node = stack.pop()
            old_to_new[node] = Node(val=node.val)

            for n in node.neighbors:
                if n not in visited:
                    visited.add(n)
                    stack.append(n)
        for old_node, new_node in old_to_new.items():
            for nei in old_node.neighbors:
                new_node.neighbors.append(old_to_new[nei])
        return old_to_new[start]


