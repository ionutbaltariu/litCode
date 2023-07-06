# Definition for a binary tree root.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root

        if p.val == root.val or q.val == root.val:
            return root

        if root.left:
            if root.left.val == p.val and q.val > root.val:
                return root
        if root.right:
            if root.right.val == q.val and p.val < root.val:
                return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None:
            return left
        else:
            return right

