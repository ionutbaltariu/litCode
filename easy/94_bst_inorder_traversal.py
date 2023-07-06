from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []

        def helper(node):
            if not node:
                return

            helper(node.left)
            inorder.append(node.val)
            helper(node.right)

        helper(root)
        return inorder
