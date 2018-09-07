import unittest

import leet343_integer_break as integer_break


class Test343(unittest.TestCase):

    def test_integer_break(self):
        expected = [1, 36]

        for entry, input in enumerate(integer_break.myinput):
            self.assertEqual(integer_break.leetSolve(input), expected[entry])
