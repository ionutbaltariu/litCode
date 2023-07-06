from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []

        q = deque()
        stack = deque()
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

            stack.append(level)

        while stack:
            levels.append(stack.pop())
        # reverse the list. Equivalent is to do a stack and then just consume it while putting elements in a list.
        return levels
