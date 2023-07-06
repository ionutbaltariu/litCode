# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorder = []

        def helper(node):
            if not node:
                return

            helper(node.left)
            inorder.append(node.val)
            helper(node.right)

        helper(root)

        l, r = 0, len(inorder) - 1

        while l < r:
            s = inorder[l] + inorder[r]

            if s == k:
                return True

            if s < k:
                l += 1
            else:
                r -= 1

        return False
