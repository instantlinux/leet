import unittest

import leet001_two_sum as two_sum


class Test001(unittest.TestCase):

    def test_two_sum(self):
        expected = [
            (0, 1),
            (1, 4)]
        for entry, input in enumerate(two_sum.myinput):
            self.assertEqual(two_sum.leetSolve(input[0], input[1]),
                             expected[entry])

    def test_two_sum_exception(self):
        with self.assertRaises(ValueError):
            two_sum.leetSolve([1, 3, 5], 9)
