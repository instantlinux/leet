"""binary_tree_paths (257)

Description:
  See https://leetcode.com/problems/binary-tree-paths/description/
"""

from lib.binarytree import BinaryTree

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
    tree = BinaryTree()
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


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(input))
