"""single_number_ii (137)

Given a non-empty array of integers, every element appears three times
except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you
implement it without using extra memory?

Examples:

  Input: [2,2,3,2]
  Output: 3

  Input: [0,1,0,1,0,1,99]
  Output: 99

"""

myinput = [
    [2, 2, 3, 2],
    [0, 1, 0, 1, 0, 1, 99]]


def leetSolve(nums):
    """single_number_ii algorithm

    Obvious way

    Args:
        nums (list): list of integers
    Returns:
        int: solo entry
    """
    result = {}
    for num in nums:
        if (num in result and result[num] == 2):
            del result[num]
        elif (num in result):
            result[num] += 1
        else:
            result[num] = 1
    return result.keys()[0]


def leetSolveClever(nums):
    """single_number_ii algorithm

    More-clever way: state table for 2-bit matrix

    current   incoming  next
    a b            c    a b
    1 0            0    1 0
    0 1            1    1 0

    Args:
        nums (list): list of integers
    Returns:
        int: solo entry
    """
    a = b = 0
    for c in nums:
        temp = (~a & b & c) | (a & ~b & ~c)
        b = (~a & ~b & c) | (~a & b & ~c)
        a = temp
    return a | b


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(input))
