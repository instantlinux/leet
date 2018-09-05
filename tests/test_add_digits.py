import unittest

import leet258_add_digits as add_digits


class Test258(unittest.TestCase):

    def test_add_digits(self):
        expected = [2]

        for entry, x in enumerate(add_digits.myinput):
            self.assertEqual(add_digits.leetSolve(x), expected[entry])
