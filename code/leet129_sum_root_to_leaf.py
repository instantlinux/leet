"""sum_root_to_leaf (129)

Description:
  See https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
"""

from lib.binarytree import BinaryTree

myinput = [
    [1, 2, 3],
    [4, 9, 0, 5, 1]]


def leetSolve(nums):
    """Find leaf paths

    Obvious way

    Args:
        nums: list of integers to build tree
    Returns:
        list: list of root-to-leaf path strings
    """

    result = 0
    # TODO: balanced tree instead of search (sorted) tree
    tree = BinaryTree()
    for item in nums:
        tree.add(item)
    for item in tree:
        if (not item.left and not item.right):
            sum = 0
            magnitude = 1
            node = item
            while (node):
                sum = sum + node.val * magnitude
                magnitude *= 10
                node = node.parent
            result += sum
    return result


for entry, input in enumerate(myinput):
    print 'case %d: %s' % (entry + 1, leetSolve(input))
