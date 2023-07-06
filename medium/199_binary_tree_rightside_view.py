from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rightside = []
        bfs_queue = deque()
        bfs_queue.append(root)

        while bfs_queue:
            # this is the last element in the level.. the rightmost element
            rightside.append(bfs_queue[-1].val)

            # this is a level, we go through the nodes at the current level and put their children
            # in the queue in order to prepare the next level
            for i in range(len(bfs_queue)):
                node = bfs_queue.popleft()

                if node.left:
                    bfs_queue.append(node.left)
                if node.right:
                    bfs_queue.append(node.right)

        return rightside
