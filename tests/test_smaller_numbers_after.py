import unittest

import leet315_smaller_numbers_after as smaller_numbers_after


class Test315(unittest.TestCase):

    def test_smaller_numbers_after(self):
        expected = [2, 1, 1, 0]

        for entry, input in enumerate(smaller_numbers_after.myinput):
            self.assertEqual(smaller_numbers_after.leetSolve(
                input, expected[entry]))

    def test_smaller_numbers_after_clever(self):
        expected = [2, 1, 1, 0]

        for entry, input in enumerate(smaller_numbers_after.myinput):
            self.assertEqual(smaller_numbers_after.leetSolveClever(
                input, expected[entry]))
