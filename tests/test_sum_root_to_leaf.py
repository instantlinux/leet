import unittest

import leet129_sum_root_to_leaf as sum_root_to_leaf


class Test129(unittest.TestCase):

    def test_sum_root_to_leaf(self):
        expected = [123, 896]

        for entry, input in enumerate(sum_root_to_leaf.myinput):
            self.assertEqual(sum_root_to_leaf.leetSolve(input),
                             expected[entry])
