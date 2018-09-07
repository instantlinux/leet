"""add_digits (258)

Given a non-negative integer num, repeatedly add all its digits until
the result has only one digit.

Example:
  Input: 38
  Output: 2

Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.

Follow up:
  Could you do it without any loop/recursion in O(1) runtime?

"""

myinput = [38]


def leetSolve(num):
    """add_digits algorithm

    Obvious way

    Args:
        num (integer): non-negative number
    Returns:
        int: sum of digits as specified
    """
    digits = list(str(num))
    sum = 0
    for digit in digits:
        sum += int(digit)
    return sum if sum < 10 else leetSolve(sum)


def leetSolveClever(num):
    """add_digits algorithm

    More-clever way: TODO

    Args:
        sumRange (tuple): first/last array indices
    Returns:
        int: sum of array contents
    """
    pass


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(input))
