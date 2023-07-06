# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        q = deque()
        q.append((root, None))

        while q:
            # we store the nodes in this level in a dictionary with the parent as the value
            level = {}
            for _ in range(len(q)):
                node, parent = q.popleft()

                if node.left:
                    q.append((node.left, node.val))
                if node.right:
                    q.append((node.right, node.val))

                level[node.val] = parent

            if x in level and y in level and level[x] != level[y]:
                return True

        return False
