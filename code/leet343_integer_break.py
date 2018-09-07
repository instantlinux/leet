# -*- coding: utf-8 -*-

"""integer_break (343)

Given a positive integer n, break it into the sum of at least two
positive integers and maximize the product of those integers. Return
the maximum product you can get.

Examples:

  Input: 2
  Output: 1
  Explanation: 2 = 1 + 1, 1 × 1 = 1.

  Input: 10
  Output: 36
  Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
"""

myinput = [2, 10]


def leetSolve(num):
    """integer_break algorithm

    Obvious way
    TODO: need to figure out the math

    Returns:
        int:  maximum product as defined
    """
    pass


for entry, input in enumerate(myinput):
    print "list %d: %s" % (entry + 1, leetSolve(input))
