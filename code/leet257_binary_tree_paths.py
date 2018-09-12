"""binary_tree_paths (257)

Description:
  See https://leetcode.com/problems/binary-tree-paths/description/
"""

myinput = [
    [1, 2, 5, 3, 6, 10, 13, 8],
    [1000],
    []]


def leetSolve(nums):
    """Find leaf paths

    Obvious way

    Args:
        nums: list of integers to build tree
    Returns:
        list: list of root-to-leaf path strings
    """

    result = []
    tree = Tree()
    for item in nums:
        tree.add(item)
    for item in tree:
        if (not item.left and not item.right):
            rootPath = []
            node = item
            while (node):
                rootPath.append(node.val)
                node = node.parent
            result.append('->'.join([str(item)
                                     for item in reversed(rootPath)]))
    return result


class Tree(object):
    def __init__(self, root=None):
        """Create a tree
        """
        self.root = root

    def add(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, root, val, parent=None):
        if root is None:
            return Tree.Node(val, parent=parent)
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
        return 'Tree(%s)' % repr(self.root)

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


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(input))
