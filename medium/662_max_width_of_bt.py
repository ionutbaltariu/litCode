from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        max_width = 1
        if not root:
            return 0

        q.append(root)

        while q:
            level = deque()

            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    level.append(node.val)
                else:
                    if len(level) != 0:
                        level.append(node)

                if not node:
                    q.append(None)
                    q.append(None)
                else:
                    q.append(node.left)
                    q.append(node.right)

            while len(level) and level[-1] is None:
                level.pop()

            current_width = len(level)

            if current_width == 0:
                break

            if current_width > max_width:
                max_width = current_width

        return max_width


if __name__ == "__main__":
    print(Solution().widthOfBinaryTree(
        TreeNode(3, left=TreeNode(2, left=TreeNode(7)), right=TreeNode(4, left=TreeNode(10)))))

