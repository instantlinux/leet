import unittest

import leet057_insert_interval as insert_interval


class Test057(unittest.TestCase):

    def test_insert_interval(self):
        expected = [
            [[1, 5], [6, 9]],
            [[1, 2], [3, 10], [12, 16]]]

        for entry, x in enumerate(insert_interval.myinput):
            self.assertEqual(insert_interval.leetSolve(x['intervals'],
                                                       x['newInterval']),
                             expected[entry])
