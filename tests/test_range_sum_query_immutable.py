import unittest

import leet303_range_sum_query_immutable as range_sum_query_immutable


class Test303(unittest.TestCase):

    def setUp(self):
        self.expected = [1, -1, -3]
        self.instance = range_sum_query_immutable.Leet303(
            range_sum_query_immutable.myinput1)

    def test_range_sum_query_immutable(self):

        for entry, x in enumerate(range_sum_query_immutable.myinput2):
            self.assertEqual(self.instance.leetSolve(x), self.expected[entry])

    def test_range_sum_query_immutable_clever(self):

        for entry, x in enumerate(range_sum_query_immutable.myinput2):
            self.assertEqual(self.instance.leetSolveClever(x),
                             self.expected[entry])
