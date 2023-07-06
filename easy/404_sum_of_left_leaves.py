from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(root, s, is_left_child=False):
    if root.left and root.right:
        return s + traverse(root.left, s) + traverse(root.right, s, True)
    elif root.left:
        return s + traverse(root.left, s)
    elif root.right:
        return s + traverse(root.right, s, True)
    else:
        return root.val if not is_left_child else 0


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0
        return traverse(root, 0)
