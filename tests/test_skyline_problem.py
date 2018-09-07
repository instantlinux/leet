import unittest

import leet218_skyline_problem as skyline_problem


class Test218(unittest.TestCase):

    def test_skyline_problem(self):
        expected = [
            [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8), (24, 0)]]

        for entry, input in enumerate(skyline_problem.myinput):
            self.assertEqual(skyline_problem.leetSolve(input),
                                                        expected[entry])
