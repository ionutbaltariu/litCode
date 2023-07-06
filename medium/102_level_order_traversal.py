from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []

        q = deque()
        q.append(root)

        while q:
            level = []
            # everything at the current level
            for i in range(len(q)):
                element = q.popleft()
                level.append(element.val)

                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)

            levels.append(level)

        return levels