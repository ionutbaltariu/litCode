from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], less_than=inf, larger_than=-inf) -> bool:
        if not root:
            return True

        if not (larger_than < root.val < less_than):
            return False

        return self.isValidBST(root.left, root.val, larger_than) and self.isValidBST(root.right, less_than, root.val)
