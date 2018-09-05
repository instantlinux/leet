import unittest

import leet153_min_in_rotated_sorted as min_in_rotated_sorted


class Test153(unittest.TestCase):

    def test_max_subarray(self):
        expected = [1, 0, 7]
        for entry, x in enumerate(min_in_rotated_sorted.myinput):
            self.assertEqual(min_in_rotated_sorted.leetSolve(x),
                             expected[entry])
