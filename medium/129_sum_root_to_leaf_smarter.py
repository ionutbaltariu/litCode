from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode], current_val=0) -> int:
        # finished branch
        if not root:
            return 0

        # this current_val works like building a number by getting its digits. First multiply with 10, then add the
        # next digit.
        current_val = current_val * 10 + root.val

        # reached leaf, can return the final value
        if not root.left and not root.right:
            return current_val

        return self.sumNumbers(root.left, current_val) + self.sumNumbers(root.right, current_val)
