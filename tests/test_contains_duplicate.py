import unittest

import leet217_contains_duplicate as contains_duplicate


class Test217(unittest.TestCase):

    def test_contains_duplicate(self):
        expected = [True, False, True]
        for entry, x in enumerate(contains_duplicate.myinput):
            self.assertEqual(contains_duplicate.leetSolve(x),
                             expected[entry])
