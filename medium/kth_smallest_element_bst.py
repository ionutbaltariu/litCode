from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # the inorder traversal (in the context of a BST) results in a list of ordered elements
        inorder = []

        def helper(node):
            if not node:
                return

            helper(node.left)
            inorder.append(node.val)
            helper(node.right)

        helper(root)
        return inorder[k - 1]
