from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # recursively, we just have to traverse the tree until we find a leaf and create the new node
        # otherwise we just update the left and right children so that we know they'll contain the new val

        # we reached a leaf
        if not root:
            return TreeNode(val)

        # decide where to keep traversing to find the good spot
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        # and just return the node
        return root
