import unittest

import leet217_contains_duplicate as contains_duplicate


class Test217(unittest.TestCase):

    def test_contains_duplicate(self):
        expected = [True, False, True]
        for entry, input in enumerate(contains_duplicate.myinput):
            self.assertEqual(contains_duplicate.leetSolve(input),
                             expected[entry])
