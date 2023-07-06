from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def helper(root, before=""):
            if not root.left and not root.right:
                paths.append(f"{before}->{root.val}"[2:])

            if root.left:
                helper(root.left, f"{before}->{root.val}")
            if root.right:
                helper(root.right, f"{before}->{root.val}")

        helper(root)
        return paths