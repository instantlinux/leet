# -*- coding: utf-8 -*-

"""range_sum_query_immutable (303)

Given an integer array nums, find the sum of the elements between
indices i and j (i ≤ j), inclusive.

Example:
  Given nums = [-2, 0, 3, -5, 2, -1]

  sumRange(0, 2) -> 1
  sumRange(2, 5) -> -1
  sumRange(0, 5) -> -3

Note:
  You may assume that the array does not change.
  There are many calls to sumRange function.
"""

myinput1 = [-2, 0, 3, -5, 2, -1]
myinput2 = [(0, 2), (2, 5), (0, 5)]


class Leet303(object):
    def __init__(self, nums):
        self.nums = nums

        # Build pre-calculated sums
        tally = 0
        self.precalc = [tally]
        for num in nums:
            tally += num
            self.precalc.append(tally)

    def leetSolve(self, sumRange):
        """range_sum_query_immutable algorithm

        Obvious way

        Args:
            sumRange (tuple): first/last array indices
        Returns:
            int: sum of array contents
        """
        sum = 0
        for num in self.nums[sumRange[0]:sumRange[1] + 1]:
            sum += num
        return sum

    def leetSolveClever(self, sumRange):
        """range_sum_query_immutable algorithm

        More-clever way: use pre-calculated values

        Args:
            sumRange (tuple): first/last array indices
        Returns:
            int: sum of array contents
        """
        return self.precalc[sumRange[1] + 1] - self.precalc[sumRange[0]]


instance = Leet303(myinput1)
for entry, x in enumerate(myinput2):
    print "list %d: %s" % (entry + 1, instance.leetSolveClever(x))
