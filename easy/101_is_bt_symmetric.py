from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEqual(self, p, q):
        if (not p and q) or (not q and p):
            return False
        if not p and not q:
            return True

        return p.val == q.val and self.isEqual(p.left, q.left) and self.isEqual(p.right, q.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True

        if (root.left and not root.right) or (root.right and not root.left):
            return False

        # flip right
        root.right = self.invertTree(root.right)

        return self.isEqual(root.left, root.right)

