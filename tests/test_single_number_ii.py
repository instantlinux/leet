import unittest

import leet137_single_number_ii as single_number_ii


class Test137(unittest.TestCase):

    def test_single_number_ii(self):
        expected = [3, 99]

        for entry, input in enumerate(single_number_ii.myinput):
            self.assertEqual(single_number_ii.leetSolve(input),
                             expected[entry])
