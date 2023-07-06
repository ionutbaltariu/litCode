from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        from_left = True
        bfs_queue = deque()
        bfs_queue.append(root)
        traversal = []

        while bfs_queue:
            level = []
            for i in range(len(bfs_queue)):

                node = bfs_queue.popleft()
                level.append(node.val)

                if node.left:
                    bfs_queue.append(node.left)
                if node.right:
                    bfs_queue.append(node.right)

            if not from_left:
                level = level[::-1]
            traversal.append(level)
            from_left = not from_left

        return traversal