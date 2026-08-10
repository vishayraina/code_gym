"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hmap = {}
        def dfs(node):
            if not node:
                return
            root = Node(node.val)
            hmap[node] = root
            neighbors = []
            for n in node.neighbors:
                if n in hmap:
                    neighbors.append(hmap[n])
                else:
                    neighbors.append(dfs(n))
            root.neighbors = neighbors
            return root
        return dfs(node)
        