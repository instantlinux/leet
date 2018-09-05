"""two-sums (1)

Given an array of integers, return indices of the two numbers such
that they add up to a specific target.

You may assume that each input would have exactly one solution, and
you may not use the same element twice.

Example:

  Given nums = [2, 7, 11, 15], target = 9,

  Because nums[0] + nums[1] = 2 + 7 = 9,
  return [0, 1].
"""

myinput = [
    ([2, 7, 11, 15], 9),
    ([1, 2, 99, 48, 7, 11, 15], 9)]


def leetSolve(items, target):
    """two-sum algorithm

    Returns:
        tuple:  indices of two list elements which add up to target
    """

    for i, val1 in enumerate(items):
        if val1 < target:
            # Only perform secondary scan if item is less than target
            for j, val2 in enumerate(items[i:]):
                if (val1 + val2 == target):
                    return (i, i + j)
    raise ValueError('No solution found')


for entry, x in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(x[0], x[1]))
