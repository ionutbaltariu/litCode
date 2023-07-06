import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    def _search(self, node, val):
        if not node:
            return False
        if node.val == val:
            return True
        if val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

    def search_value(self, val):
        return self._search(self.root, val)

    def print_preorder(self):
        def _preorder(node):
            if node:
                print(node.val, end=' ')
                _preorder(node.left)
                _preorder(node.right)

        print("preorder:", end=' ')
        _preorder(self.root)
        print()

    def print_inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.val, end=' ')
                _inorder(node.right)

        print("inorder:", end=' ')
        _inorder(self.root)
        print()

    def print_postorder(self):
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                print(node.val, end=' ')

        print("postorder:", end=' ')
        _postorder(self.root)
        print()

    def insert_node(self, val):
        def _insert(node, val):
            if not node:
                return TreeNode(val)

            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)

            return node

        _insert(self.root, val)

    def get_leaves(self):
        leaves = []

        def helper(node):
            if not node:
                return

            if not node.left and not node.right:
                leaves.append(node.val)

            helper(node.left)
            helper(node.right)

        helper(self.root)
        return leaves

    def remove_node(self, val):
        def _remove(node, val):
            if not node:
                return

            if val < node.val:
                node.left = _remove(node.left, val)
            elif val > node.val:
                node.right = _remove(node.right, val)
            else:
                # leaf
                if not node.left and not node.right:
                    node = None
                elif node.left and not node.right:
                    node = node.left
                elif node.right and not node.left:
                    node = node.right
                # every value should work
                else:
                    current = node.right

                    while current.left:
                        current = current.left

                    node.val = current.val
                    node.right = _remove(node.right, current.val)

            return node

        _remove(self.root, val)

    def bfs(self):
        queue = collections.deque()
        queue.append(self.root)
        traversal = []

        while len(queue):
            n = queue.popleft()
            traversal.append(n.val)

            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)

        return traversal




if __name__ == "__main__":
    tree = TreeNode(7, left=TreeNode(5, left=TreeNode(3, left=TreeNode(2)), right=TreeNode(6)),
                    right=TreeNode(9, right=TreeNode(12, left=TreeNode(11, left=TreeNode(10)))))
    # search_tree = BinarySearchTree(tree)
    search_tree = BinarySearchTree(TreeNode(3, left=TreeNode(2, left=TreeNode(1)), right=TreeNode(5, right=TreeNode(7, left=TreeNode(6), right=TreeNode(9)))))
    search_tree.print_inorder()
    # search_tree.remove_node(5)
    search_tree.print_inorder()
    print(search_tree.bfs())
    # search_tree.search_value(5)
    # search_tree.print_preorder()
    # search_tree.print_inorder()
    # search_tree.print_postorder()
    # search_tree.insert_node(8)
    # search_tree.print_inorder()
    # search_tree.remove_node(8)
    # search_tree.print_inorder()
