import unittest

import leet202_happy_number as happy_number


class Test202(unittest.TestCase):

    def test_happy_number(self):
        expected = [True, False, False, True]

        for entry, input in enumerate(happy_number.myinput):
            self.assertEqual(happy_number.leetSolve(input),
                             expected[entry])

    def test_happy_number_clever(self):
        expected = [True, False, False, True]

        for entry, input in enumerate(happy_number.myinput):
            self.assertEqual(happy_number.leetSolveClever(input),
                             expected[entry])
