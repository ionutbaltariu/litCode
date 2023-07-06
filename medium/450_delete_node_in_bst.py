# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # leaf
            if not root.left and not root.right:
                root = None
            elif root.left and not root.right:
                root = root.left
            elif root.right and not root.left:
                root = root.right
            else:
                current = root.right

                while current.left:
                    current = current.left

                root.val = current.val
                root.right = self.deleteNode(root.right, current.val)

        return root