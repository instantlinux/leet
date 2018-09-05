"""contains-duplicate (217)

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice
in the array, and it should return false if every element is distinct.

Examples:

  Input: [1,2,3,1]
  Output: true

  Input: [1,2,3,4]
  Output: false

  Input: [1,1,1,3,3,4,3,2,4,2]
  Output: true
"""

myinput = [
    [1, 2, 3, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]


def leetSolve(items):
    """
    Returns:
        bool:  true if dup found
    """

    for key, val in enumerate(items):
        for item in items[key + 1:]:
            if (val == item):
                return True
    return False


for entry, x in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(x))
