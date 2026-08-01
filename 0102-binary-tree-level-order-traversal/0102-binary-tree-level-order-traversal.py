# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append([root])
        res = []
        while q:
            level = q.popleft()
            l, n = [], []
            for node in level:
                if node:
                    l.append(node.val)
                    n.extend([node.left, node.right])
            if l:
                res.append(l)
            if n:
                q.append(n)
        return res
