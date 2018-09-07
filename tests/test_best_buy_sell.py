import unittest

import leet121_best_buy_sell as best_buy_sell


class Test001(unittest.TestCase):

    def test_best_buy_sell(self):
        expected = [5, 0]
        for entry, input in enumerate(best_buy_sell.myinput):
            self.assertEqual(best_buy_sell.leetSolve(input),
                             expected[entry])

    def test_best_buy_sell_clever(self):
        expected = [5, 0]
        for entry, input in enumerate(best_buy_sell.myinput):
            self.assertEqual(best_buy_sell.leetSolveClever(input),
                             expected[entry])
