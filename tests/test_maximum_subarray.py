import unittest

import leet053_maximum_subarray as maximum_subarray


class Test053(unittest.TestCase):

    def test_max_subarray(self):
        expected = [6, 99, -8]
        for entry, input in enumerate(maximum_subarray.myinput):
            self.assertEqual(maximum_subarray.leetSolve(input),
                             expected[entry])
