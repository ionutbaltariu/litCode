from collections import deque
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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False

        q = deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                popped = q.popleft()

                if popped.val == subRoot.val:
                    res = self.isEqual(popped, subRoot)

                    # if they aren't equal, it's possible that there are multiple nodes with the same value
                    # we'll try to check 'em all
                    if res is True:
                        return res

                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)

        return False
