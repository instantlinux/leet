import unittest

import leet191_number_of_1bits as number_of_1bits


class Test191(unittest.TestCase):

    def test_number_of_1bits(self):
        expected = [3, 1]

        for entry, input in enumerate(number_of_1bits.myinput):
            self.assertEqual(number_of_1bits.leetSolve(input), expected[entry])
