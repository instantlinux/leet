"""product-of-array (238)

Given an array nums of n integers where n > 1, return an array output
such that output[i] is equal to the product of all the elements of
nums except nums[i].

Example:

  Input:  [1,2,3,4]
  Output: [24,12,8,6]
  Note: Please solve it without division and in O(n).

Follow up:

  Could you solve it with constant space complexity? (The output array
  does not count as extra space for the purpose of space complexity
  analysis.)
"""

myinput = [
    [1, 2, 3, 4]]


def leetSolve(items):
    """Obvious way
    Create an output list the same length as the input list, with
    each element multiplied by the others

    Args:
        items (list): integer list
    Returns:
        list:  results
    """

    result = [1] * len(items)
    for i, val1 in enumerate(items):
        for j, val2 in enumerate(items):
            if (i != j):
                result[i] *= val2
    return result


def leetSolveClever(items):
    """More-clever way
    Create two temporary lists, pick the middle array element and
    iterate over each once. Then multiply entries from those two
    lists.

    TODO - took over 30 min

    Args:
        items (list): integer list
    Returns:
        list:  results
    """

    middle = len(items) / 2
    lower = [1] * len(items)
    upper = [1] * len(items)
    for key, val in enumerate(items[1:middle]):
        lower[key] = lower[key - 1] * items[key - 1]
    print middle
    print lower
    for key, val in reversed(list(enumerate(items[:len(items) - 1]))):
        print key
        upper[key] = upper[key + 1] * items[key + 1]
        if (key < middle):
            break
    print upper
    result = []
    for key in xrange(len(items)):
        result.append(lower[key] * upper[key])
    return result


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolveClever(input))
