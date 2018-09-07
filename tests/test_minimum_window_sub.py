import unittest

import leet076_minimum_window_sub as minimum_window_sub


class Test076(unittest.TestCase):

    def test_minimum_window_sub(self):
        expected = ['BANC']
        for entry, input in enumerate(minimum_window_sub.myinput):
            self.assertEqual(
                minimum_window_sub.leetSolve(input['s'], input['t']),
                expected[entry])
