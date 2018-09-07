"""maximum-subarray (53)

Given an integer array nums, find the contiguous subarray (containing
at least one number) which has the largest sum and return its sum.

Example:

  Input: [-2,1,-3,4,-1,2,1,-5,4],
  Output: 6
  Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
  If you have figured out the O(n) solution, try coding another
  solution using the divide and conquer approach, which is more
  subtle.

"""

myinput = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [-2, -3, 2, -1, 2, 1, -5, 99],
    [-8]]


def _sumRange(items, range):
    """
    Args:
        items (list): integer list
        range (tuple): first/last elements to sum
    Returns:
        int: sum of items in defined range
    """
    sum = 0
    for item in items[range[0]:range[1] + 1]:
        sum += item
    return sum


def leetSolve(items):
    """Finds sub-list of contiguous items with largest sum

    Obvious way

    Args:
        items (list): integer list
    Returns:
        list:  results
    """
    maxResult = 0
    for i in range(len(items) + 1):
        for j in range(i + 1, len(items) + 1):
            sum = _sumRange(items, (i, j))
            maxResult = max(sum, maxResult)
    return maxResult


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(input))
