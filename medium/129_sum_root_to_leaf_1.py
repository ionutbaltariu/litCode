# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = []

        def helper(root, what_was_before=""):
            if not root.left and not root.right:
                paths.append(what_was_before + str(root.val))
                return ""
            elif not root.left:
                return helper(root.right, what_was_before + str(root.val))
            elif not root.right:
                return helper(root.left, what_was_before + str(root.val))
            else:
                return helper(root.left, what_was_before + str(root.val)) + helper(root.right,
                                                                                   what_was_before + str(root.val))

        helper(root)
        return sum(int(x) for x in paths)