from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        copy = root

        if not root:
            return TreeNode(val)

        while True:
            if val < copy.val:
                if not copy.left:
                    copy.left = TreeNode(val)
                    return root

                copy = copy.left
            else:
                if not copy.right:
                    copy.right = TreeNode(val)
                    return root

                copy = copy.right
