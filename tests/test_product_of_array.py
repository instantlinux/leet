import unittest

import leet238_product_of_array as product_of_array


class Test238(unittest.TestCase):

    def test_product_of_array(self):
        expected = [
            [24, 12, 8, 6]]
        for entry, x in enumerate(product_of_array.myinput):
            self.assertEqual(product_of_array.leetSolve(x),
                             expected[entry])

    def test_product_of_array_clever(self):
        expected = [
            [24, 12, 8, 6]]
        for entry, x in enumerate(product_of_array.myinput):
            self.assertEqual(product_of_array.leetSolveClever(x),
                             expected[entry])
