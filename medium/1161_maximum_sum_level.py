from collections import deque
from typing import Optional
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        lvl = -1
        max_s = -inf
        current_lvl = 0

        while q:
            current_lvl += 1
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if s > max_s:
                max_s = s
                lvl = current_lvl

        return lvl
