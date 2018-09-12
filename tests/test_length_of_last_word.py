import unittest

import leet058_length_of_last_word as length_of_last_word


class Test058(unittest.TestCase):

    def test_length_of_last_word(self):
        expected = [5, 34, 0]

        for entry, input in enumerate(length_of_last_word.myinput):
            self.assertEqual(length_of_last_word.leetSolve(input),
                             expected[entry])
