"""min_in_rotated_sorted (153)

Suppose an array sorted in ascending order is rotated at some pivot
unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Examples:

  Input: [3,4,5,1,2]
  Output: 1

  Input: [4,5,6,7,0,1,2]
  Output: 0
"""

myinput = [
    [3, 4, 5, 1, 2],
    [4, 5, 6, 7, 0, 1, 2],
    [7]]


def leetSolve(items):
    """Find minimum value in a sorted array, rotated

    Obvious way

    Args:
        items (list): integer list
    Returns:
        int: minimum value
    """
    firstValue = items[0]
    for i in items[1:]:
        # As soon as we encounter a value below that of the first
        #  element, we can halt the loop
        if (i < firstValue):
            return i
    return firstValue


for entry, x in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(x))
