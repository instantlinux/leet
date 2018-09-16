"""binarytree

created 13 sep 2018 by rbraun at instantlinux.net
"""


class BinaryTree(object):
    def __init__(self, root=None):
        """Create a tree
        """
        self.root = root

    def add(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, root, val, parent=None):
        if root is None:
            return BinaryTree.Node(val, parent=parent)
        if (val < root.val):
            root.left = self._insert(root.left, val, root)
        else:
            root.right = self._insert(root.right, val, root)
        return root

    def __iter__(self):
        if (self.root is None):
            return iter([])
        else:
            return iter(self.root)

    def __repr__(self):
        return 'BinaryTree(%s)' % repr(self.root)

    class Node:
        def __init__(self, val, left=None, right=None, parent=None):
            self.val = val
            self.left = left
            self.right = right
            self.parent = parent

        def __iter__(self):
            if (self.left is not None):
                for item in self.left:
                    yield item
            yield self
            if (self.right is not None):
                for item in self.right:
                    yield item

        def __repr__(self):
            return 'Node(%s:%s,%s)' % (repr(self.val), repr(self.left),
                                       repr(self.right))
