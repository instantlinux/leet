import unittest

import leet292_nim_game as nim_game


class Test292(unittest.TestCase):

    def test_nim_game(self):
        expected = [False, True, False, True, False]

        for entry, input in enumerate(nim_game.myinput):
            self.assertEqual(nim_game.leetSolve(input),
                             expected[entry])
